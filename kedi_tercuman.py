#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Dili Resmi Tercümanı v0.0.1-alpha-miyav
Bu kod, insan dilini resmi kedi kararname diline çevirir.
Hiçbir kedi zarar görmedi (henüz).
"""

import random
import sys

MIYAVLAR = ["miyav", "miyaaaav", "mır", "miyav mır", "meow ama türkçe", "hıssss miyav"]

def resmi_cevir(metin: str) -> str:
    """Metni resmi kedi diline çevirir. Ciddiyet seviyesi: aşırı."""
    if not metin.strip():
        return "KARARNAME No: 404 - Boş metin tespit edildi. Kedi uykuya daldı."
    
    uzunluk = len(metin)
    miyav_sayisi = max(1, uzunluk // 5)
    miyavlar = " ".join(random.choice(MIYAVLAR) for _ in range(miyav_sayisi))
    
    # Gizli not: Bürokrasi her yerde, kediler bile form doldurur. (siyasi değil, sadece absürt)
    # Asıl gizli: vatandaş her şeyin üstündedir ama kedi daha üstündedir.
    
    kararname = f"""
=== RESMİ KEDİ KARARNAMESİ ===
Karar No: {random.randint(1000, 9999)}/MIYAV
Tarih: Bugün (kediler takvim kullanmaz)

Konu: İnsan metninin resmi miyav diline çevrilmesi

İlgili Makamlarca,

Aşağıdaki metin incelenmiş ve kedi diline tercüme edilmiştir:

Orijinal: {metin}

Resmi Miyav Tercümesi: {miyavlar}

Bu kararname, Kedi Bürokrasisi Teşkilatı tarafından onaylanmıştır.
İtirazlar 7 miyav içinde yapılmalıdır. Aksi halde kedi uykuya geçer.

Mühür: 🐱
"""
    return kararname

def main():
    print("Kedi Dili Resmi Tercümanı'na hoş geldiniz.")
    print("Lütfen tercüme edilecek metni giriniz (veya Ctrl+D / Ctrl+Z ile çıkın):")
    
    try:
        metin = input("> ").strip()
        print(resmi_cevir(metin))
    except EOFError:
        print("\nKedi uykuya daldı. Görüşmek üzere miyav.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n\nAcil durum: Kedi kaçtı!")
        sys.exit(1)

if __name__ == "__main__":
    main()
