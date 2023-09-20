# mind-archives

Nama    : Andi Salsabila A
NPM     : 2206083571

Tugas 3

- Apa perbedaan antara form POST dan form GET dalam Django?
   1. Post:
      - Di dalam POST, tidak ada batas jumlah data yang bisa dikirimkan dengan post request sehingga dapat digunakan untuk mengsubmit data yang lebih besar seperti pengunggahan file.
      - POST memiliki keamanan yang lebih dibandingkan GET karena mengirimkan data di HTTP request body dan tidak terlihat di dalam URL sehingga dapat menjadi pilihan tepat untuk informasi rahasia seperti password. 
      - Beberapa request POST yang identik dapat menghasilkan efek yang berbeda-beda di server.
      - POST biasanya digunakan untuk mengsubmit data yang akan membuat, memperbarui, ataupun memodifikasi resource di dalam server, seperti melakukan posting di sosial media ataupun registrasi.
   2. GET:
      - Di dalam GET, terdapat batas data yang dapat dikirimkan di satu waktu dan dapat menjadi penghambat bagi data yang besar ataupun kompleks.
      - Karena GET menambah data form ke URL sebagai parameter di dalam query, maka data dapat terlihat di address bar di browser, sehingga memiliki tingkat keamanan yang lebih rendah.
      - Beberapa request GET yang identik akan menghasilkan hasil yang sama di server.
      - GET biasanya digunakan untuk mengambil data dari server, seperti filter data, navigasi halaman, dan mencari item. GET sendiri tidak direkomendasikan untuk digunakan dalam mengubah data yang sudah berada di dalam server.

- Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   1. XML (Extensible Markup Language)
      - XML merupakan markup language yang memiliki versatilitas tinggi dan digunakan untuk mendeskripsikan dan memberikan struktur pada data
      - XML biasanya digunakan untuk mengonfigurasi file dan melakukan pertukaran data terstruktur antar sistem.
      - Meskipun tidak memiliki kinerja yang lebih baik dibandingkan JSON, XML lebih ramah digunakan oleh manusia karena sifatnya yang human-readable.
   2. JSON (JavaScript Object Notation)
      - JSON merupakan format pertukaran data yang memiliki sifat lightweight dan mudah untuk digunakan oleh manusia dan mesin untuk dibaca dan ditulis.
      - JSON merepresentasikan data sebagai pasangan key-value dictionary yang lebih cocok digunakan untuk merepresentasikan data terstruktur seperti object dan array.
      - JSON lebih mudah digunakan oleh manusia dan mesin. Meskipun begitu, diperlukan beberapa pemahaman dasar untuk memahami JSON sehingga menjadi alternatif yang sedikit lebih sulit digunakan oleh orang awam.
   3. HTML (Hypertext Markup Language)
      - HTML merupakan markup language yang digunakan untuk mendefinisikan struktur dan kerangka dari webpage.
      - HTML menggunakan tags untuk mendefinisikan elemen yang merepresentasikan bagian-bagian dari webpage, seperti heading, paragraph, dan image.
      - HTML memiliki readability yang cukup baik untuk dibaca manusia. Meskipun begitu, tujuan utama penggunaan HTML adalah untuk menginstruksikan web untuk menampilkan kerangka dasar dari sebuah webpage.

- Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   JSON sendiri merupakan format pertukaran data yang memiliki tingkat efisiensi yang tinggi untuk digunakan oleh manusia dan mesin. Selain itu, JSON sendiri dapat digunakan dengan bahasa pemrograman apa saja dan dapat menjadi pilihan yang universal untuk pertukaran data antara bagian aplikasi web yang berbeda-beda. Selain itu, JSON juga dapat menyokong penggunaan struktur data yang berbeda-beda seperti object, array, string, dan lain sebagainya. Selain itu, karena sifatnya yang human-readable, JSON sendiri lebih mudah digunakan untuk debugging dan testing, sehingga menjadi pilihan yang cocok dalam pertukaran data antara aplikasi web modern.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Di dalam direktori mind-archives yang telah saya buat, pertama-tama dilakukan aktivasi virtual environment. Setelah itu, dilakukan perubahan routing dari main/ menjadi /. Setelah itu, dilakukan implementasi Skeleton sebagai kerangka Views dengan cara menambah base.html ke dalam direktori mind-archives dan mengubah kode main.html dengan template utama dari base.html. Setelah itu, dilakukan modifikasi settings.py yang ada di dalam subdirektori shopping_list.

   Untuk membuat form input data pada HTML, berkas baru bernama forms.py dibuat untuk membuat struktur form yang dapat menerima data produk baru. Dilakukan perubahan pada views.py yang terdapat di dalam folder main dan juga penambahan beberapa fungsi di dalam berkas tersebut. Selanjutnya, dilakukan penambahan path url ke dalam urls.py di main untuk mengakses fungsi sebelumnya. Setelah itu, terdapat penambahan berkas HTML baru dengan nama create_product.html dan perubahan di dalam main.html.

   Agar dapat mengembalikan data dalam bentuk XML dan juga JSON, dilakukan beberapa perubahan dan juga penambahan fungsi di dalam views.py. Setelah itu, dilakukan import fungsi yang telah dibuat sebelumnya dan juga penambahan beberapa path url XML dan juga JSON di dalam urls.py. Setelah itu, dilakukan run server dan program dapat dijalankan di dalam localhost.