from django.shortcuts import render
from .models import AnnouncedLgaResults, Lga, Party, PollingUnit, AnnouncedPuResults
# Create your views here.


def polling_unit(request, p_u_i):
    p = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=p_u_i)
    return render(request, 'app/poll_u.html', {'results': p})

def polling_unit_ed(request, p_u_i):
    pa = Party.objects.all()
    if request.method == 'POST':
        pl = request.POST.getlist('party')
        sl = request.POST.getlist('score')
        
        for p, s in zip(pl, sl):
            
            a,_ = AnnouncedPuResults.objects.get_or_create(polling_unit_uniqueid=p_u_i, party_abbreviation=p)
            if a.party_score != s and int(s) > 0:
                a.party_score = s
                a.save()
                
            print(p, s)
    return render(request, 'app/n_poll.html', {'parties': pa})

def all_parties(request):
    pollin  = PollingUnit.objects.all()
    lga = Lga.objects.all()
     
    return render(request, 'app/index.html', {'pollin':pollin, 'lgas': lga})

def lga_f(request):
    r = 0
    lga = Lga.objects.get(uniqueid=request.GET.get('lga'))
    
    pl = PollingUnit.objects.filter(lga_id = lga.lga_id)
    for p in pl:
        for a in AnnouncedPuResults.objects.filter(polling_unit_uniqueid=p.uniqueid):
            r += int(a.party_score)
            
    r1 = 0
    alga = AnnouncedLgaResults.objects.filter(lga_name=lga.lga_name) 
           
    print(alga) 
    return render(request, 'app/lga_r.html', {'lga': lga, 'result': r, 'result1': r1})



def all_polling_unit(request):
    return render(request, 'app/all_poll.html')


