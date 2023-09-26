# mind-archives

Nama    : Andi Salsabila A
NPM     : 2206083571

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