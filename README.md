# Настройка RPtaha

## Установка образа на Raspberry Pi4

1. Скачай образ операционной системы [RP4 Bullseye](https://ln5.sync.com/dl/4083226a0/e7t6w7jp-x4vqthff-8v9fxzuh-9y84f2x4/view/default/12603243340004)**.** Более подробная информация о образе системы доступна на [github компании Q-engineering](https://github.com/Qengineering/RPi-Bullseye-DNN-image). Если ссылка для скачивания образа будет не доступна, то скачай его с [Яндекс Диска](https://disk.yandex.ru/d/jI3tcIIIQy1Wuw).
2. Установи [balenaEtcher](https://balena-etcher.com/) и запиши с её помощью образ полученный в первом пункте на микро SD-карту. Помни, что объем памяти карты должен быть не менее 16 Gb. 
3. Вставь микро SD-карту в Raspberry Pi4.  Подожди несколько минут, пока образ распакуется до полного размера SD-карты.
4. Обнови системные пакеты до крайних версий. 
    
    ### Важно!
    
    - Имя пользователя: pi
    - Пароль: 3.14
    
    Имя пользователя и пароль не требуются для входа в систему, но нужны для подключения с помощью VNC. Поэтому их лучше запомнить. 
    
    ### Советы:
    
    - По умолчанию Raspberry Pi разогнан до 1850 МГц. Дополнительную информацию смотри в разделе [разгон Raspberry Pi](https://qengineering.eu/overclocking-the-raspberry-pi-4.html).
    - Если нужно дополнительное место на SD-карте, то можно удалить папки opencv и opencv и opencv_contrib. В них больше нет необходимости, поскольку все библиотеки размещены в каталоге /usr/local.
    - Установи VScode с помощью утилиты Recommended Software
        
        ![Снимок экрана от 2023-09-02 21-36-55.png](Images/screenshot.png)
        
## Подключение Raspberry PI4 как компаньен компьютер
Информация по подключению Raspberry PI к автопилоту   [здесь](https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html).

## Установка зависимостей
Желательно устанавливать библиотеки из под виртуального окружения для исключения проблем с зависимостями, но это не обязательно.

1. Установи [picamera2](https://github.com/raspberrypi/picamera2) (репа для работы с камерой в Bullseye).
    ```bash
    sudo apt install -y python3-picamera2
    ```
    Или через pip
    ```bash
    sudo apt install -y python3-libcamera python3-kms++
    sudo apt install -y python3-prctl libatlas-base-dev ffmpeg libopenjp2-7 python3-pip
    pip3 install numpy --upgrade
    pip3 install picamera2
    ```
2. Установи [DroneKit](https://github.com/dronekit/dronekit-python)

    ```bash
    pip3 install dronekit
    ```

    OpenCV уже должна стоять в системе из коробки.


## Запуск тестового скрипта
Запусти скрипт rptaha.py для проверки. Он захватывает изображение с камеры и получает от автопилота:
- угловые положения roll, pith, yaw; 
- скорости по X, Y, Z (в системе NED); 
- текущую высоту altitude;

затем рисует крест в центре изображения и выводит его на экран.


## КАКАЯ ПОМОЩЬ НАМ НУЖНА

1. Получение параметров с помощью [PyMavlink](https://github.com/ArduPilot/pymavlink) со скоростью не ниже 30 Hz (примеры того что мы пробовали лежат в файле test_pymavlink.py)
2. Возможно мы неправильно настроили канал телеметрии на самом автопилоте, поэтому необходима помощь с его натройкой (но это только догадки). В качестве прошивки мы используем Ardupilot.
3. Возможно, если есть время, то написать краткую доку по использованию Pymavlink.





