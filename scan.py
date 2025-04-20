import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=ajdRvxDWH4w&list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW&ab_channel=ShradhaKhapra")
img.save("apnajava_youtube.png")