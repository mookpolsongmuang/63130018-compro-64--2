print("this is a vaccine selector program.")
print("Has this patient receive any prior vaccination? (1=yes,3=no)")
n = input("Yes/No")
n = int(n)
if n < 2:
    print("this patient receive -1 shot of pfeizer vaccine-")
if n > 2:
    print("Has this patient been infected with Sars-cov 2 virus before(1=yes,3=no)")
o = input("Yes/No")
o = int(o)
if o < 2:
    print("this patient receive -1 shot of pfeizer vaccine-")
if o > 2:
    print("this patient receive -2 shot of pfeizer vaccine-")
