from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context
#from scrape.forms import 
from scrape.models import scraper
from scrape.Scrape2SQL import setup_clean_scrape, scrapefct, renderScrapeSite
import sqlite3
                    
def home(request):

    html = renderScrapeSite()
    page = HttpResponse(html)
    
    if request.method == 'POST':
        if request.POST.get('scrapeOrder'):
            return HttpResponseRedirect('scrape.views.please_wait')
            #scrapefct()
    """
        elif request.POST.get('cleanDbOrder'):
            setup_clean_scrape()
            html = renderScrapeSite(1)
            return HttpResponseRedirect(html)
        elif request.POST.get('updateDbOrder'):
            #update function
            html = renderScrapeSite(1)
            return HttpResponseRedirect(html)
        elif request.POST.get('liveScrapeOrder'):
            #activate script with auto_refresh = 600 with an update
            html = renderScrapeSite(1)
            return HttpResponseRedirect(html)
        """
    """
    #return page
    datab = sqlite3.connect('weightedAvg.db')
    with datab:
        cursor = datab.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS WAvg(id INT, spot_date TEXT, hour TEXT, weighted_avg REAL);")
        cursor.execute("SELECT * FROM WAvg ORDER BY id")
        rows = cursor.fetchall()
        return render_to_response(request, '/templates/home.html/', {'data':rows})
    """
    return page

    
def scraper(request, scraper_id):
    if request.method == 'POST':
        choice = Choice.objects.get(id=request.POST['vote'])
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('scrape.views.scraper', args=[scraper_id,]))
    Scp = scraper.objects.get(pk=scraper_id)
    form = ScrapeSubmitButtonField(Scp=Scp)
    return render(request, 'scraper.html', {'scraper': Scp, 'form': form})

def please_wait(request):
    html = "<html><body>Please wait while database repopulates</body></html>"
    return HttpResponse(html)
