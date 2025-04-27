# Gerekli Kütüphaneler
import cv2
import numpy as np

# 1. Görseli yükleme
image = cv2.imread('image.jpeg')  # Görseli oku (kendi görsel yolunu yazın)
if image is None:
    print("Görsel yüklenemedi. Lütfen dosya yolunu kontrol edin.")
    exit()

# 2. Görseli gri tonlamaya çevirme
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. HSV tonlamasını elde etme
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 4. Renk kanallarını değiştirme (B ile R)
# OpenCV'de görseller BGR formatında okunur, bu yüzden B ve R kanallarını değiştiriyoruz
swapped_image = image.copy()
swapped_image[:, :, 0], swapped_image[:, :, 2] = image[:, :, 2], image[:, :, 0]

# 5. Görselin altına ad yazdırma
# Önce görselleri birleştireceğiz (orijinal, gri, hsv, swapped)
# Tüm görselleri aynı boyuta getirme (HSV ve BGR swapped görseller 3 kanallı)
gray_image_3ch = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Görselleri yan yana birleştirme
top_row = np.hstack((image, gray_image_3ch))
bottom_row = np.hstack((hsv_image, swapped_image))
combined_image = np.vstack((top_row, bottom_row))

# Adı yazdırma
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(combined_image, 'Emin Can', (10, combined_image.shape[0] - 30), 
            font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Sonucu gösterme
cv2.imshow('Islemler ve Ad', combined_image)

# Sonucu kaydetme
cv2.imwrite('processed_image.jpg', combined_image)

# Pencereleri kapatmak için bir tuşa basmayı bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()