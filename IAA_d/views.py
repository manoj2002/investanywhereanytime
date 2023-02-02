import json
import pandas as pd
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import buysdata, activitysdata
from django.shortcuts import render, redirect
from .tiingo import get_meta_data,get_price_data,get_today_data,get_intraday_data
from datetime import datetime

def home(request):
    return render(request,'IAA_d/home.html',{'title':'IAA-HOME'})

def stocks(request, tid):
    t=tid
    dd=get_meta_data(tid)
    dt=get_price_data(tid)
    td=get_today_data(tid)
    hd=get_intraday_data(tid)
    return render(request,'IAA_d/stocks.html', {'t':t,'dd':dd,'dt':dt,'td':td,'title':'IAA-Stock','hd':hd})

def trade(request):
    df = pd.read_csv('IAA_d/static/csv/supported_tickers.csv')
    df1 = df
    dd = df1.sample(n=20, replace=True)
    json_records = dd.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    if request.method=='POST' and request.user.is_authenticated:
            ticker=request.POST['ticker']
            return HttpResponseRedirect(ticker)
    elif request.user.is_authenticated:
        return render(request, 'IAA_d/trade.html', {'title': 'IAA-Trade', 'd': data})
    else:
        return redirect("login")
def buystock(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        dd=get_meta_data(ticker)
        td = get_today_data(ticker)
        print(td)
        for i in td:
            to=i['open']
        return render(request,'IAA_d/buystock.html',{'t':ticker,'dd':dd,'title':'IAA-BuyStock','td':to})
    return render(request,'IAA_d/buystock.html',{'title':'IAA-BuyStock'})
def buydata(request):
    if request.method=='POST':
        username=request.POST['username']
        ticker=request.POST['tick_data']
        ticker=ticker.upper()
        Quantity=request.POST['quantity']
        q=int(Quantity)
        name=request.POST['tick_name']
        o = buysdata.objects.all()
        c=0
        for i in o:
            if i.username == username and i.ticker==ticker :
                i.quantity=i.quantity+int(Quantity)
                i.save()
                c=1
                desc="stock updated with quantity"
                break
        if c==0:
            bsd = buysdata(username=username, name=name,ticker=ticker, quantity=Quantity)
            bsd.save()
            desc="stock bought with quantity"
        dti=datetime.now()
        act = activitysdata(username=username, desc=desc, name=name, ticker=ticker, quantity=q,dtime=dti)
        act.save()
        messages.success(request, "Stock Buy Success")
    return redirect('trade')
def sellstock(request):
    d=[]
    to=[]
    o=buysdata.objects.all()
    for i in o:
        if i.username==request.user.username:
            print(str(i.id)+" "+i.username+" "+i.ticker+" "+str(i.quantity))
            d.append(i)
            print(d)
            td = get_today_data(i.ticker)
            for j in td:
                to.append(j['close'])
    return render(request,"IAA_d/sellstock.html",{'title':'IAA-sellStock','data':d,'td':to})
def selldata(request):
    if request.method=='POST':
        username=request.POST['username']
        ticker=request.POST['ticker']
        ticker=ticker.upper()
        Quantity=request.POST['quantity']
        name=request.POST['name']
        q=int(Quantity)
        o = buysdata.objects.all()
        desc="stock sold of quantity"
        for i in o:
            if i.username == username and i.ticker==ticker :
                if int(Quantity)>=i.quantity:
                    i.delete()
                else:
                  i.quantity=i.quantity-int(Quantity)
                  i.save()
                break
        dti=datetime.now()
        act=activitysdata(username=username,desc=desc,name=name,ticker=ticker,quantity=q,dtime=dti)
        act.save()
        messages.success(request, "Stock sell Success")
    return redirect('sellstock')
def activity(request):
    d=[]
    a=activitysdata.objects.all()
    for i in a:
        if i.username==request.user.username:
            d.append(i)
    return render(request,"IAA_d/activity.html",{'title':'IAA-Activity','data':d})
