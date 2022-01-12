from django.contrib.auth import get_user_model, admin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from accounts.models import Mezun, Ogrenci, OgretimGorevlisi, BolumSekreteri




from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'grafik/charts.html', {})

User = get_user_model()

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #Mezun Çalışma Oranı
        qs_count = Mezun.objects.all().count()
        qs_count2= Mezun.objects.filter(calismaDurumu = 'Çalışıyorum').count()
        qs_count3 = Mezun.objects.filter(calismaDurumu = 'Çalışmıyorum').count()

        #Kullanıcı Dağılımı

        k_count2 = Mezun.objects.all().count()
        k_count3 = Ogrenci.objects.all().count()
        k_count4 = OgretimGorevlisi.objects.all().count()
        k_count5 = BolumSekreteri.objects.all().count()

        #Şehirlere Göre Çalışma Oranı

        s_count = Mezun.objects.filter(calismaDurumu = 'Çalışıyorum').count()
        s_count2 = Mezun.objects.filter(il = 'trabzon').count()
        s_count3 = Mezun.objects.filter(il = 'samsun').count()
        s_count4 = Mezun.objects.filter(il = 'istanbul').count()
        s_count5 = Mezun.objects.filter(il = 'bursa').count()
        s_count6 = Mezun.objects.filter(il = 'ankara').count()
        s_count7 = Mezun.objects.filter(il = 'balıkesir').count()
        s_count8 = Mezun.objects.filter(il = 'izmir').count()
        s_count9 = Mezun.objects.filter(il = 'kocaeli').count()
        s_count10 = Mezun.objects.filter(il = 'eskişehir').count()
        s_count11 = Mezun.objects.filter(il = 'sakarya').count()
        s_count12 = Mezun.objects.filter(il = 'adana').count()
        s_count13 = Mezun.objects.filter(il = 'artvin').count()
        s_count14 = Mezun.objects.filter(il = 'aydın').count()
        s_count15 = Mezun.objects.filter(il = 'denizli').count()
        s_count16 = Mezun.objects.filter(il = 'erzurum').count()
        s_count17 = Mezun.objects.filter(il = 'mersin').count()
        s_count18 = Mezun.objects.filter(il = 'ısparta').count()
        s_count19 = Mezun.objects.filter(il = 'manisa').count()
        s_count20 = Mezun.objects.filter(il = 'ordu').count()
        s_count21 = Mezun.objects.filter(il = 'nevşehir').count()
        s_count22 = Mezun.objects.filter(il = 'rize').count()
        s_count23 = Mezun.objects.filter(il = 'sivas').count()
        s_count24 = Mezun.objects.filter(il = 'sinop').count()

        #Sektörlere göre dağılım

        i_count = Mezun.objects.filter(sektor= 'Akademik').count()
        i_count2 = Mezun.objects.filter(sektor = 'Ambalaj').count()
        i_count3 = Mezun.objects.filter(sektor = 'Araştırma ve Geliştirme').count()
        i_count4 = Mezun.objects.filter(sektor = 'Yazılım ve Bilişim').count()
        i_count5 = Mezun.objects.filter(sektor = 'Danışmanlık').count()
        i_count6 = Mezun.objects.filter(sektor = 'Demir ve Çelik').count()
        i_count7 = Mezun.objects.filter(sektor = 'Elektrik ve Elektronik').count()
        i_count8 = Mezun.objects.filter(sektor = 'Enerji').count()
        i_count9 = Mezun.objects.filter(sektor = 'Gıda').count()
        i_count10 = Mezun.objects.filter(sektor = 'Havacılık').count()
        i_count11 = Mezun.objects.filter(sektor = 'Hazır Giyim').count()
        i_count12 = Mezun.objects.filter(sektor = 'Holding ve Şirketler Grubu').count()
        i_count13 = Mezun.objects.filter(sektor = 'Isıtma, Havalandırma ve Klima').count()
        i_count14 = Mezun.objects.filter(sektor = 'İletişim').count()


        i_count15 = Mezun.objects.filter(sektor = 'İnşaat').count()
        i_count16 = Mezun.objects.filter(sektor = 'Kimya Sanayi').count()
        i_count17 = Mezun.objects.filter(sektor = 'Logistik').count()
        i_count18 = Mezun.objects.filter(sektor = 'Makine ve Ekipmanları').count()
        i_count19 = Mezun.objects.filter(sektor = 'Metal Sanayi').count()
        i_count20 = Mezun.objects.filter(sektor = 'Oto Yedek Parça ve Yan Sanayi').count()
        i_count21 = Mezun.objects.filter(sektor = 'Otomotiv').count()
        i_count22 = Mezun.objects.filter(sektor = 'Plastik ve Ürünleri').count()
        i_count23 = Mezun.objects.filter(sektor = 'Sağlık').count()
        i_count24 = Mezun.objects.filter(sektor = 'Tekstil').count()
        i_count25 = Mezun.objects.filter(sektor = 'Turizm ve Medya').count()
        i_count26 = Mezun.objects.filter(sektor = 'Üretim ve Endüstriyel Ürünler').count()
        i_count27 = Mezun.objects.filter(sektor = 'Yapı').count()
        i_count28 = Mezun.objects.filter(sektor = 'Diğer').count()

        ## Ünvan ve Mesleklere Göre Dağılım

        m_count = Mezun.objects.filter(unvanMeslek = 'Doçent').count()
        m_count2 = Mezun.objects.filter(unvanMeslek='Endüstri Mühendisi').count()
        m_count3 = Mezun.objects.filter(unvanMeslek='Fabrika Müdürü').count()
        m_count4 = Mezun.objects.filter(unvanMeslek='İhracat Müşteri temsilcisi').count()
        m_count5 = Mezun.objects.filter(unvanMeslek='İmalat Müdürü').count()
        m_count6 = Mezun.objects.filter(unvanMeslek='Kalite Güvence Müdürü').count()
        m_count7 = Mezun.objects.filter(unvanMeslek='Kalite Güvence Mühendisi').count()
        m_count8 = Mezun.objects.filter(unvanMeslek='Mühendis').count()
        m_count9 = Mezun.objects.filter(unvanMeslek='Öğretim Görevlisi').count()
        m_count10 = Mezun.objects.filter(unvanMeslek='Planlama Müdürü').count()
        m_count11 = Mezun.objects.filter(unvanMeslek='Planlama Mühendisi').count()

        m_count12 = Mezun.objects.filter(unvanMeslek='Planlama Sorumlusu').count()
        m_count13 = Mezun.objects.filter(unvanMeslek='Profesör').count()
        m_count14 = Mezun.objects.filter(unvanMeslek='Proje Satış Uzmanı').count()
        m_count15 = Mezun.objects.filter(unvanMeslek='Satın Alma Mühendisi').count()
        m_count16 = Mezun.objects.filter(unvanMeslek='Satış Mühendisi').count()
        m_count17 = Mezun.objects.filter(unvanMeslek='Satış Pazarlama Sorumlusu').count()
        m_count18 = Mezun.objects.filter(unvanMeslek='Üretim Mühendisi').count()
        m_count19 = Mezun.objects.filter(unvanMeslek='Üretim Planlama Müdürü').count()
        m_count20 = Mezun.objects.filter(unvanMeslek='Üretim Planlama Mühendisi').count()
        m_count21 = Mezun.objects.filter(unvanMeslek='Üretim Planlama Sorumlusu').count()
        m_count22 = Mezun.objects.filter(unvanMeslek='Diğer').count()

        labels6 = ["Doçent", "Endüstri Mühendisi", "Fabrika Müdürü","İhracat Müşteri Temsilcisi","İmalat Müdürü","Kalite Güvence Müdürü","Kalite Güvence Mühendisi",
                   "Mühendis","Öğretim Görevlisi","Planlama Müdürü","Planlama Mühendisi"]
        default_items6 = [m_count,m_count2,m_count3,m_count4,m_count5,m_count6,m_count7,m_count8,m_count9,m_count10,m_count11]

        labels7 = ["Planlama Sorumlusu","Profesör","Proje Satış Uzmanı","Satın Alma Mühendisi","Satış Mühendisi","Satış Pazarlama Sorumlusu","Üretim Mühendisi",
                   "Üretim Planlama Müdürü","Üretim Planlama Mühendisi","Üretim Planlama Sorumlusu","Diğer"]
        default_items7 = [m_count12,m_count13,m_count14,m_count15,m_count16,m_count17,m_count18,m_count19,m_count20,m_count21,m_count22]



        labels = ["Mezun", "Çalışan", "Çalışmayan"]
        default_items = [qs_count, qs_count2, qs_count3]

        labels2 = ["Mezun", "Öğrenci", "Öğretim Üyesi", "Sekreter"]
        default_items2 = [k_count2, k_count3, k_count4, k_count5]

        labels3 = ["Mezun", "Trabzon", "Samsun", "İstanbul", "Bursa", "Ankara", "Balıkesir", "İzmir", "Kocaeli",
                   "Eskişehir", "Sakarya", "Adana", "Artvin", "Aydın", "Denizli",
                   "Erzurum", "Mersin", "Isparta", "Manisa", "Ordu", "Nevşehir", "Rize", "Sivas", "Sinop"]
        default_items3 = [s_count, s_count2, s_count3, s_count4, s_count5, s_count6, s_count7, s_count8, s_count9,
                          s_count10, s_count11, s_count12, s_count13, s_count14, s_count15,
                          s_count16, s_count17, s_count18, s_count19, s_count20, s_count21, s_count22, s_count23,
                          s_count24]

        labels4 = ["Akademik", "Ambalaj", "Araştırma ve Geliştirme", "Yazılım ve Bilişim", "Danışmanlık", "Demir-Çelik",
                   "Elektrik & Elektronik", "Enerji", "Gıda","Havacılık", "Hazır Giyim", "Holding/Şirketler Grubu", "Isıtma,Havalandırma ve Klime", "İletişim"]
        default_items4 = [i_count, i_count2, i_count3, i_count4, i_count5, i_count6, i_count7, i_count8, i_count9,i_count10,
                          i_count11, i_count12, i_count13, i_count14]

        labels5 =["İnşaat", "Kimya Sanayi", "Logistik", "Makine","Metal Sanayi", "Mobilya", "Oto Yedek Parça", "Otomotiv", "Plastik ve Ürünleri", "Sağlık", "Tekstil", "Turizm ve Medya","Üretim/Endüstriyel Ürünler", "Yapı", "Diğer"]
        default_items5=[i_count15,i_count16, i_count17, i_count18, i_count19, i_count20, i_count21, i_count22, i_count23,
                          i_count24,i_count25, i_count26, i_count27, i_count28]

        labels6 = ["Doçent", "Endüstri Mühendisi", "Fabrika Müdürü","İhracat Müşteri Temsilcisi","İmalat Müdürü","Kalite Güvence Müdürü","Kalite Güvence Mühendisi",
                   "Mühendis","Öğretim Görevlisi","Planlama Müdürü","Planlama Mühendisi"]
        default_items6 = [m_count,m_count2,m_count3,m_count4,m_count5,m_count6,m_count7,m_count8,m_count9,m_count10,m_count11]

        labels7 = ["Planlama Sorumlusu","Profesör","Proje Satış Uzmanı","Satın Alma Mühendisi","Satış Mühendisi","Satış Pazarlama Sorumlusu","Üretim Mühendisi",
                   "Üretim Planlama Müdürü","Üretim Planlama Mühendisi","Üretim Planlama Sorumlusu","Diğer"]
        default_items7 = [m_count12,m_count13,m_count14,m_count15,m_count16,m_count17,m_count18,m_count19,m_count20,m_count21,m_count22]

        data = {
                "labels": labels,
                "default": default_items,

                "labels2" : labels2,
                "default2":default_items2,

                "labels3" : labels3,
                "default3" : default_items3,

                "labels4" : labels4,
                "default4" : default_items4,

                "labels5" : labels5,
                "default5" : default_items5,

                "labels6" : labels6,
                "default6" : default_items6,

                "labels7" : labels7,
                "default7" : default_items7,
        }
        return Response(data)

