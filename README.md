# mind-archives

Nama    : Andi Salsabila A
NPM     : 2206083571

Tugas 2

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
   Tugas 2 dimulai dengan membuat folder baru bernama mind-archives. Setelah itu, saya mulai mengaktifkan virtual environment untuk membuat proyek Django dan membuat aplikasi main sebagai konfigurasi awal untuk memulai proyek.

   Setelah itu, dilakukan implementasi model dasar, mengaplikasikan migrasi model, dan juga menghubungkan views dengan template. Untuk memberikan unsur estetika di dalam Tugas 2 ini, saya mengimplementasikan CSS yang digabungkan ke dalam HTML untuk memberikan perubahan dari segi user interface. Terdapat penambahan model yang dimodifikasi sesuai dengan ketentuan tugas, seperti Item yang memiliki atribut name, amount, dan description. Selain itu, terdapat beberapa atribut tambahan yang ada di dalam model tersebut seperti date added dan juga artist.

   Setelah dilakukan migrasi untuk model ini, function yang ditujukan untuk menampilkan nama, nama aplikasi, dan kelas dibuat di dalam views.py. Selanjutnya, dilakukan routing URL pada aplikasi main agar nantinya dapat dilakukan deployment melalui Adaptable. Meskipun begitu, terdapat beberapa kendala di dalam proses deployment disebabkan terjadinya pemblokiran akun yang biasa digunakan oleh saya untuk mendeploy tugas oleh Adaptable, sehingga proses deployment untuk tugas ini masih belum dapat dilakukan.

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![IMG_9042477C4657-1](https://github.com/stronovski/mind-archives/assets/74691199/94dada2c-331e-4fa3-8cc7-328e2732b2d4)

- Jelaskan mengapa kita menggunakan virtual environment?
   Dengan menggunakan virtual environment, terdapat kemudahan dalam menjaga beberapa versi python yang memiliki perbedaan di masing-masing versi tersebut seperti library dan juga dependency untuk tetap terpisah dari satu sama lain. Karena terdapat error prevention dengan adanya pemisahan tersebut, pembuatan proyek Django dengan beberapa versi yang berbeda menjadi lebih mudah dan aman dan mengurangi kemungkinan terjadinya clash ataupun error.

 - Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Meskipun pada dasarnya proyek Django dapat dibuat tanpa menggunakan virtual environment, terdapat  resiko terjadinya clash ataupun error yang lebih tinggi, terutama jika pengguna mengerjakan beberapa proyek aplikasi Django dengan versi Python yang berbeda-beda dan juga memiliki library dan juga dependency yang berbeda di satu waktu, sehingga hal tersebut tidak dianjurkan untuk dilakukan.

- Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   1. MVC (Model-View-Controller) adalah design pattern yang memisahkan aplikasi menjadi tiga komponen yang berbeda untuk memisahkan pekerjaan yang masing-masing komponen lakukan. Model merepresentasikan data aplikasi, View merepresentasikan user interface, dan Controller yang menjadi sebuah komponen perantara antara Model dan View dan menangani request dari user.

   2. MVT (Model-View-Template) memiliki pembagian tiga komponen, yaitu Model yang merepresentasikan data aplikasi, View yang merepresentasikan user interface, dan Template yang mendefinisikan bagaimana data dari Model diproses di View dan dispesifikasikan melalui struktur HTML. Dibandingkan untuk memproses interaksi dan input pengguna, Template lebih berfokus untuk mendefinisikan presentasi data. Salah satu framework yang menggunakan design pattern ini adalah Django.

   3.  MVVM (Model-View-Viewmodel) memiliki tiga pembagian komponen, yaitu Model yang merepresentasikan data aplikasi, View yang merepresentasikan user interface, dan ViewModel yang merupakan perantara antara Model dan View dan memperlihatkan data dan command yang bisa dilekatkan pada View. Terdapat penekanan mengenai data binding di design pattern ini, di mana perubahan pada ViewModel dapat langsung terlihat di View dan juga sebaliknya.

maaf kak saya izin telat mengumpulkan karena harus mengikuti gemastik kemarin t___t