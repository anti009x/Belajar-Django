from django.shortcuts import render, redirect
from adminmodule.models import Toko
from django.contrib import messages
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def adminview(request):
  data=Toko.objects.all()
  context={"data":data}
  return render (request,'dashboard.html',context)

def UpdateData(request, id):
    if request.method == "POST":
        nama_toko = request.POST['nama_toko']
        pemilik = request.POST['pemilik']
        tahun_berdiri = request.POST['tahun_berdiri']
        jenis_toko = request.POST['jenis_toko']
        print(nama_toko, pemilik, tahun_berdiri, jenis_toko)

        # Simpan data ke dalam database
        query = Toko.objects.get(id=id)
        query.nama_toko = nama_toko
        query.pemilik = pemilik
        query.tahun_berdiri = tahun_berdiri
        query.jenis_toko = jenis_toko
        query.save()
        messages.success(request, "data berhasil di update")
        return redirect('adminview')  # Mengarahkan ke dashboard.html

    i = Toko.objects.get(id=id)
    context = {"i": i}
    return render(request, 'edit.html', context)

def DeleteData(request,id):
  i = Toko.objects.get(id=id)
  i.delete()
  messages.success(request, "data berhasil dihapus")
  return redirect('adminview')


@requires_csrf_token

def insertData(request):
    data=Toko.objects.all()
    context={"data":data}
    if request.method == "POST":
        nama_toko = request.POST.get('nama_toko')
        pemilik = request.POST.get('pemilik')
        tahun_berdiri = request.POST.get('tahun_berdiri')
        jenis_toko = request.POST.get('jenis_toko')

        # Simpan data ke dalam database
        query = Toko(nama_toko=nama_toko, pemilik=pemilik, tahun_berdiri=tahun_berdiri, jenis_toko=jenis_toko)
        query.save()
        messages.success(request, "Data Terkirim")
        return redirect ('adminview')

    return render (request,'dashboard.html',context)
    
