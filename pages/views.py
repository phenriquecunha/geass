from django.views.generic import TemplateView
from django.db.models.functions import Coalesce
from django.db.models import Sum

import datetime
import calendar
from scheduling.models import Detour



class DashBoardView(TemplateView):
    template_name = 'home.html'

    def get_detour_year_month(self):
        data = []
        try:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            for m in range(1, 13):
                TotalDevationPerMonth = Detour.objects.filter(date__year=year, date__month=m).aggregate(r=Coalesce(Sum('detour'), 0)).get('r')
                if m == month:
                    averagePerMonth = TotalDevationPerMonth / day
                else:
                    monthRange = calendar.monthrange(year, m)
                    averagePerMonth = TotalDevationPerMonth / monthRange[1]
                data.append(round(averagePerMonth, 2))
        except:
            pass

        return data

    def get_average_detour(self):
        filter: str = self.request.GET.get('filter') if self.request.GET.get('filter') else '30'
        totalDevation = Detour.objects.filter(date__gt=datetime.datetime.now()-datetime.timedelta(days=int(filter))).aggregate(r=Coalesce(Sum('detour'), 0)).get('r')
        averageDetour = totalDevation / int(filter)

        return round(averageDetour, 2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['averageDetour'] = self.get_average_detour
        context['detourYearMonth'] = self.get_detour_year_month
        return context
        

