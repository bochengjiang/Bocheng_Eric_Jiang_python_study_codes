import numpy as np
import matplotlib.pyplot as plt

def double_slit_interference(width, distance, wavelength, screen_distance, screen_size):
    x = np.linspace(-screen_size/2, screen_size/2, 1000)
    
    # 两个狭缝的干涉项
    interference_term = np.cos((2 * np.pi * width * x) / (wavelength * screen_distance))
    
    # 总的光强分布
    intensity = (1 + interference_term) ** 2
    
    # 绘制干涉图样
    plt.plot(x, intensity)
    plt.xlabel('屏幕上的位置')
    plt.ylabel('光强')
    plt.title('双缝干涉')
    plt.show()

# 例子：双缝干涉
double_slit_interference(width=0.1, distance=0.5, wavelength=0.0005, screen_distance=1.0, screen_size=0.2)
