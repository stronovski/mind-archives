# mind-archives

Nama    : Andi Salsabila A
NPM     : 2206083571

tautan: http://andi-salsabila21-tugas.pbp.cs.ui.ac.id/

## Tugas 5
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming dan asynchronous programming merupakan paradigma pemrograman yang memiliki perbedaan dalam segi penanganan eksekusi atau operasi. Di dalam synchronous programming, operasi dieksekusi satu per satu sehingga harus menunggu operasi yang lain selesai dijalankan agar dapat menjalankan operasi selanjutnya. Selain itu, synchronous programming dapat juga mengimplementasikan thread untuk melakukan beberapa operasi dalam satu waktu yang ada di dalam proses utama. Sedangkan di asynchronous programming, tidak terdapat blocking sehingga operasi tidak harus menunggu operasi lain selesai. Selain itu, terdapat konsep event-driven yang memungkinkan program mengeksekusi instruksi tanpa menunggu hasil, kemudian hasil ditangani secara asinkron setelah selesai.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan pendekatan pemrograman di mana events memengaruhi eksekusi program secara keseluruhan. Hal ini bertujuan agar program dapat memproses interaksi pengguna agar dapat menerima respon terhadap kejadian tertentu. Penggunaan AJAX yang digunakan saat pengguna mengklik tombol "add products by AJAX" yang merupakan sebuah event listener merupakan salah satu contoh penerapan dari event-driven programming di dalam tugas ini.

### Jelaskan penerapan asynchronous programming pada AJAX.
Karena operasi yang terlibat di dalam data server memerlukan waktu yang tidak mudah diprediksi, maka AJAX melakukan pendekatan asynchronous programming yang tidak memerlukan blocking sehingga dapat menjalankan operasi yang melibatkan pengambilan data dari server. Dengan hal ini, terdapat berbagai fungsi yang menerapkan asynchronous programming, seperti callbacks yang merupakan parameter penanda yang akan dijalankan setelah suatu operasi selesai.

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API dan library JQuery merupakan kedua teknologi yang dapat diimplementasikan untuk menerapkan AJAX. Meskipun begitu, keduanya memiliki beberapa kelebihan dan kekurangannya masing-masing. Fetch API merupakan bagian dari JavaScript yang tidak memerlukan extension atau pengunduhan library tambahan untuk diterapkan. Selain itu, Fetch API pun menggunakan konsep promise yang dapat menangani dan menghindari callback hell dan juga lebih ringan untuk digunakan. Meskipun begitu, Fetch API memerlukan polyfill agar dapat diterapkan untuk browser yang lebih outdated.

JQuery sendiri merupakan utility library yang telah menyiapkan banyak fungsi untuk membantu implementasi di dalam pemrograman, seperti animasi dan banyak lagi. Selain itu, JQuery menggunakan callback untuk menangani respon dan juga lebih mendukung untuk browser yang lebih outdated.

Penggunaan keduanya pun bergantung terhadap kebutuhan masing-masing. Jika memerlukan banyak utilitas di dalam program tersebut dan juga perlu mendukung keperluan untuk browser yang outdated, JQuery dapat dijadikan pilihan yang tepat, sedangkan Fetch API digunakan untuk proyek yang hanya memerlukan asynchronous operation dan berfokus kepada browser modern karena sifatnya yang memenuhi standar modern.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama, buat beberapa fungsi baru seperti add_product_ajax yang menerima parameter request dan juga menambahkan dekorator @csrf_exempt. Setelah itu, lakukan routing untuk fungsi get_product_json dan add_product_ajax di dalam urls.py. Tampilkan data product dengan menggunakan fetch() API dan buat beberapa kode yang mengimplementasikan struktur card dan buat block script dan tambahkan function getProducts dan refreshProducts. Untuk mengimplementasikan modal sebagai form, gunakan bootstrap agar dapat memberikan tampilan dari modal. Setelah itu, buat fungsi baru bernama addProduct() di dalam block script. Setelah semua step yang dilakukan di atas selesai dijalankan, maka aplikasi web pun dapat menerapkan AJAX dan menampilkan modal sebagai form :3

## Tugas 4
### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Terdapat beberapa element selector, seperti element selector, class selector, ID selector, dan attribute selector. Keempatnya memiliki fungsi masing-masing seperti berikut:
- Class Selector:
class selector digunakan untuk memilih semua elemen yang memiliki atribut class yang spesifik, sehingga dapat digunakan untuk mengaplikasikan style ke elemen-elemen berbeda yang memiliki class yang sama dan juga untuk membuat style dari grup elemen menjadi lebih konsisten.

- Element Selector: 
element selector digunakan untuk memilih semua elemen dari tipe yang ada dan digunakan untuk mengaplikasikan sebuah style secara universal ke suatu elemen dari HTML.

- ID Selector
id selector digunakan untuk mengaplikasikan syle ke sebuah atribut id yang spesifik, sehingga lebih sering digunakan untuk mengganti style sebuah elemen yang lebih khusus dan unik dibandingkan dengan elemen-elemen lain.

- Attribute Selector
attribute selector memilih elemen berdasarkan value dari atribut yang mereka miliki dan digunakan untuk memilih elemen dengan atribut yang spesifik.

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
<header> : merupakan container untuk elemen-elemen yang berada di paling atas. header sendiri dapat berisi beberapa hal seperti navigasi, perkenalan web, hero, dan lain sebagainya.
<footer> : merupakan container untuk elemen-elemen yang berada di paling bawah.
<nav>: digunakan untuk mengisi elemen-elemen yang merupakan navigation links
<audio>: digunakan untuk meng-embed audio stream di dalam dokumen HTML.

### 3. Jelaskan perbedaan antara margin dan padding.
Margin merupakan space elemen yang dapat memberikan ruang di luar border, sehingga dapat memberikan jarak antara satu elemen dengan elemen yang lain.
Padding merupakan space yang dapat memberikan ruang pada area di dalam border. Padding sendiri dapat memiliki background dari elemen tersebut, sehingga kerap kali digunakan untuk pembuatan button dan lain sebagainya.

### 4.  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Bootstrap merupakan CSS Framework yang melakukan pendekatan high-level bagi pengguna. Karena sifatnya yang lebih mudah, Bootstrap lebih ramah digunakan bagi pemula karena adanya komponen dan style yang telah ditentukan sebelumnya. Meskipun begitu, Bootstrap tidak memiliki fleksibilitas yang tinggi dibandingkan dengan Tailwind dan dapat menghasilkan ukuran file menjadi lebih besar karena adanya berbagai variasi style dan komponen yang digunakan. Bootstrap dapat digunakan jika pengembang ingin membuat suatu aplikasi web yang membutuhkan waktu yang sedikit untuk dikembangkan dan juga tidak memiliki elemen design yang memiliki signifikansi tinggi untuk dikustomisasi.

Tailwind merupakan CSS Framework yang memiliki fleksibilitas tinggi karena dapat dikustomisasi sesuai dengan keinginan developer. Selain itu, Tailwind hanya membutuhkan size yang lebih kecil dibandinkan dengan Bootstrap karena hanya melibatkan style yang digunakan. Meskipun begitu, Tailwind memiliki tingkat kesulitan yang lebih tinggi bagi pemula dan memiliki learning curve yang lebih curam. Tailwind dapat digunakan ketika aplikasi web yang ingin dikembangkan memerlukan fleksibilitas desain dan juga kuasa penuh atas desain web yang akan dibentuk.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk mengimplementasikan checklist yang ada, pertama-tama, saya mengubah tampilan pada setiap page dengan menggunakan internal CSS dengan bantuan Bootstrap. Dengan hal ini, saya mengganti berbagai komponen yang ada di dalam main seperti warna, font, dan lain sebagainya. Setelah itu, saya menyesuaikan padding dan margin sesuai dengan kebutuhan. Selain itu, header, hero, dan footer juga ditambahkan di masing-masing page yang akan digunakan jika pengguna telah melakukan login dengan adanya Bootstrap. Untuk mengimplementasikan elemen-elemen desain di dalam tugas ini, diperlukan berbagai trial-and-error untuk memastikan bahwa desain aplikasi web sesuai dengan visi yang ingin dituju. 

## Tugas 3

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm merupakan salah satu _built-in authentication system_ yang digunakan di dalam pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan ini, _developer_ dapat dengan mudah membuat suatu program yang dapat mengizinkan pengguna untuk membuat registrasi _user_ di suatu aplikasi tertentu.

Django UserCreationForm memiliki beberapa kelebihan yang dapat dijadikan pertimbangan untuk mengimplementasikan sistem autentikasi ini. UserCreationForm dapat memudahkan _developer_ untuk mengembangkan programnya tanpa perlu membuat semua program dari nol. Karena hal tersebut, _developer_ dapat menggunakan waktunya untuk meng-_handle_ bagian lain yang diperlukan di dalam program tersebut. Selain itu, UserCreationForm juga menawarkan keamanan optimal untuk otorisasi dan autentikasi pengguna yang dapat membantu mencegah masalah keamanan. UserCreationForm juga dapat dikustomisasi sesuai dengan kebutuhan aplikasi ataupun fitur yang ingin diterapkan oleh pengembang web.

Kekurangan yang terdapat di dalam UserCreationForm adalah adanya limitasi dari fleksibilitas _developer_ karena UserCreationForm bisa saja tidak dapat mengakomodasi kebutuhan web yang diperlukan sehingga aspek-aspek tersebut dapat memberikan batasan bagi _developer_ untuk membuat fitur autentikasi yang dibutuhkan. Selain itu, karena UserCreationForm sendiri merupakan sistem autentikasi bawaan Django, jika seandainya pengembang mengganti _framework_ untuk keperluan pengembangan maka akan membutuhkan banyak modifikasi terhadap program yang telah dibuat karena sifatnya yang _dependent_ terhadap Django Framework.


### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi di dalam Django merujuk ke proses bagaimana sebuah sistem dapat memverifikasi identitas pengguna untuk memastikan bahwa pengguna yang sedang mencoba masuk merupakan pengguna sah yang memiliki hak untuk mengakses fitur-fitur atau aksi tertentu di dalam suatu aplikasi. Django sendiri memiliki sistem autentikasi bawaan seperti sistem untuk _login_, _logout_, dan juga _register_.

Otorisasi merupakan batasan hak suatu pengguna untuk mengakses fitur atau menjalankan suatu aksi di suatu peramban web. Otorisasi sendiri mendefinisikan apa yang dapat dilakukan ataupun yang tidak bisa dilakukan oleh pengguna di dalam akses peramban web tertentu.  Sebagai contoh, suatu nasabah bank hanya dapat mengakses saldo ataupun melakukan transfer dari akunnya sendiri dan tidak dapat menjalankan aksi tersebut di akun milik orang lain. Di dalam Django, terdapat @login_required yang mengharuskan pengguna untuk melakukan _login_ agar dapat mengakses segala fitur yang ada di dalam aplikasi yang digunakan pengguna.

Autentikasi dan otorisasi memiliki signifikansi yang sangat penting untuk memastikan keamanan pengguna. Autentikasi mencegah terjadinya kebocoran data yang memungkinkan data dari pengguna untuk jatuh ke tangan orang lain, sedangkan otorisasi menjaga kontrol atas apa yang dapat dilakukan pengguna untuk memastikan bahwa pengguna hanya memiliki akses data dari akun milik masing-masing dan melakukan tindakan yang sesuai dengan peran mereka.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

_Cookies_ adalah _text file_ yang memiliki bagian kecil dari data yang digunakan untuk mengidentifikasi komputer yang digunakan pengguna. Ketika _cookie_ melakukan pertukaran data antara komputer dan juga _server network_, server akan membaca ID dan mengetahui apa saja informasi yang dibutuhkan pengguna untuk mengetahui preferensi dan analisis perilaku pengguna. Django sendiri menggunakan _cookies_ untuk mengelola data sesi pengguna untuk menyimpan keadaan sesi di aplikasi web.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

_Cookies_ sendiri merupakan protokol yang digunakan untuk berkomunikasi antara pengguna dan server. Meskipun pada umumnya penggunaan _cookies_ tidak berbahaya, terdapat beberapa potensi keamanan yang dapat terjadi di dapat terjadi, di antaranya adalah _cookie theft_ dengan mencuri atau menggunakan _cookies_ pengguna lain, memanipulasi _cookies_ untuk mengakses data-data yang tidak diperbolehkan diakses oleh orang lain, dan juga memiliki kekhawatiran mengenai penggunaan privasi pengguna

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Untuk dapat mengimplementasikan _checklist_ yang telah dibuat, terdapat beberapa langkah yang harus dilakukan. Pertama-tama, dilakukan _import_ beberapa _built-in registration system_ ke dalam views.py untuk memudahkan pembuatan formulir pengguna di dalam aplikasi web, seperti:

'''
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
'''

Setelah itu, dilakukan penambahan fungsi bernama register di dalam views.py yang akan berisi formulir registrasi secara otomatis dan membuat akun pengguna setelah data yang dimasukkan pengguna di-_submit_ ke dalam form.

'''
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
'''

Setelah itu, dilakukan pembuatan berkas HTML baru dengan nama register.html di dalam folder main/templates yang bertujuan untuk menampilkan kerangka dari laman _register_ ketika pengguna sedang mencoba untuk melakukan registrasi.

'''
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
'''

Setelah itu, dilakukan penambahan import fungsi register di dalam urls.py dan juga menambahkan _path url_ untuk mengakses fungsi yang telah diimpor tadi.

'''
from main.views import register

app_name = 'main'

urlpatterns = [
      ...
      path('register/', register, name='register'),
      ...
'''

Setelah dilakukan penambahan fitur registrasi, dilakukan penambahan fitur login. Di dalam views.py, _import_ beberapa _built-in authentication and login system_ yang ada di dalam Django, seperti:

'''
from django.contrib.auth import authenticate, login
'''

Setelah itu, terdapat penambahan fungsi login_user di dalam views.py yang bertujuan untuk mengautentikasi pengguna yang ingin login.

'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
'''

Setelah itu, dilakukan penambahan berkas HTML baru pada folder main/templates yang bernama login.html yang berisi kerangka web ketika pengguna sedang mencoba untuk login.

'''
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
'''

Setelah dilakukan beberapa penambahan tersebut, dilakukan _routing_ di dalam urls.py dengan mengimpor fungsi yang telah dibuat di dalam views.py

'''
from main.views import login_user

app_name = 'main'

urlpatterns = [
      ...
      path('login/', login_user, name='login'),
      ...
'''

Untuk mengimplementasikan pembuatan fungsi logout, _import built-in logout system_ yang ada di dalam Django ke dalam views.py, seperti:

'''
from django.contrib.auth import logout
'''

Setelah itu, dilakukan penambahan fungsi logout_user di dalam views.py

'''
def logout_user(request):
    logout(request)
    return redirect('main:login')
'''

Setelah itu, tambahkan potongan kode berikut di dalam main.html untuk memunculkan sebuah button yang memungkinkan pengguna untuk melakukan logout:

'''
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
'''

Setelah itu, dilakukan penambahan import fungsi logout di dalam urls.py dan juga menambahkan _path url_ untuk mengakses fungsi yang telah diimpor tadi.

'''
from main.views import logout_user

app_name = 'main'

urlpatterns = [
      ...
      path('logout/', logout_user, name='logout'),
      ...
'''

Untuk merestriksi akses halaman main, dilakukan _import_ pada 'views.py' dan tambahkan kode '@login_required(login_url='/login')' di atas fungsi 'show_main':

'''
from django.contrib.auth.decorators import login_required
'''

Untuk dapat menggunakan data dari _cookies_, dilakukan beberapa _import_ di dalam 'views.py', yaitu 'import datetime'. Setelah itu, pada fungsi login_user, ganti kode yang ada di dalam login_user sebagai berikut:

'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
'''

Kemudian pada fungsi show_main, terdapat penambahan kode seperti berikut:

'''
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'THE MIND ARCHIVES',
        'name': request.user.username, # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'products': products,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)
'''

Kemudian dilakukan pengubahan fungsi logout_user menjadi berikut:

'''
...
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
...
'''

Di dalam berkas main.html, tambahkan potongan kode berikut di antara tabel dan tombol logout untuk menampilkan data last login:

'''
<h5>Sesi terakhir login: {{ last_login }}</h5>
'''

Setelah itu, untuk menghubungkan model Product dengan User, dilakukan import di dalam 'models.py':

'''
from django.contrib.auth.models import User
'''

Kemudian, dilakukan penambahan variable user di dalam class Product:

'''
...
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
'''

Setelah itu, ubah potongan fungsi 'create_product' di dalam 'views.py' menjadi berikut:

'''
...
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
'''

Kemudian, ubah fungsi 'show_main' menjadi berikut:

'''
...
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
'''

Di dalam tugas bonus, terdapat penambahan tombol dan fungsi untuk menambahkan dan mengurangi amount produk sebanyak satu. Untuk mengimplementasikan fungsi ini, dibuat 2 fungsi di dalam views.py sebagai berikut:

'''
...
def add_amount(request, pk):
    product = Product.objects.get(id = pk)
    product.amount += 1
    product.save()
    return HttpResponseRedirect('/')

def sub_amount(request, pk):
    product = Product.objects.get(id = pk)
    if not (product.amount <= 0):
        product.amount -= 1
    product.save()
    return HttpResponseRedirect('/')

...
'''

Setelah itu, _import_ kedua fungsi tersebut ke dalam urls.py sehingga dapat terlihat sebagai berikut:

'''
from main.views import add_amount, sub_amount
'''

Kemudian, tambahkan path berikut ke dalam urlpatterns

'''
...
urlpatterns = [
    path('add_amount/<str:pk>/', add_amount, name='add_amount'),
    path('sub_amount/<str:pk>/', sub_amount, name='sub_amount')
]
...
'''

Setelah itu, tambahkan dua tombol yang dapat menambah ataupun mengurangi produk di antara product.amount di dalam file main.html seperti berikut:

'''
...
        <td>
            <a href="{% url 'main:add_amount' product.id %}">
                <button>
                    +
                </button>
            </a> 

            {{product.amount}}

            <a href="{% url 'main:sub_amount' product.id %}">
                <button>
                    -
                </button>
            </a> 
        </td>
...
'''

Untuk mengimplementasikan tombol dan fungsi untuk menghapus suatu objek dari inventori, pertama-tama dilakukan penambahan fungsi di dalam views.py sebagai berikut:

'''
...
def sub_amount(request, pk):
    product = Product.objects.get(id = pk)
    if not (product.amount <= 0):
        product.amount -= 1
    product.save()
    return HttpResponseRedirect('/')
...
'''

Setelah itu, lakukan _import_ fungsi tersebut ke dalam urls.py

'''
...
from main.views import product_delete
'''

Setelah itu, tambahkan path ke dalam urlpatterns sebagai berikut:

'''
...
urlpatterns = [
   ...
    path('product_delete/<str:pk>/', product_delete, name='product_delete'),
    ...
]
'''

Setelah itu, tambahkan tombol tersebut di akhir setiap baris dalam tabel

'''
...
        <td> 
            <a href="{% url 'main:product_delete' product.id %}">
                <button>
                    Delete Product
                </button>
            </a> 
        </td>
...
'''

Setelah itu, 2 akun baru yang berisi 3 produk dibuat untuk keperluan soal. Setelah semua step yang dilakukan di atas selesai dijalankan, maka aplikasi web pun dapat menerapkan fitur login, logout, register, mengimplementasikan cookie, membuat button yang dapat merubah nilai dari suatu produk, dan juga membuat button yang dapat menghapus produk :3