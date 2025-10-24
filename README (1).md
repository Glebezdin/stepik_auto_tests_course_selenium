# Scolio NFC

**Scolio NFC** — мобильное приложение для работы с NFC-датчиками.  
Проект реализует две версии приложения — для врачей и пациентов, а также предоставляет отдельную библиотеку для взаимодействия с NFC-датчиками.

---

## Архитектура проекта

### 1. Core Module (`ru.scolio.nfc.core`)
Базовый модуль с общими компонентами, используемыми в обоих приложениях.

#### Основные компоненты:
- **Account Manager**
  - Управление аккаунтами пользователей (доктор / пациент)
  - Работа с `SharedPreferences`
  - Поддержка типов аккаунтов: `DoctorAccount`, `PatientAccount`

- **Error Handler**
  - Централизованная обработка ошибок
  - Композитная система обработчиков

- **Message Manager**
  - Управление UI-сообщениями (`Snackbar`, `AlertDialog`)
  - Унифицированный API для уведомлений

- **Extensions**
  - Расширения для работы с датами
  - Расширения для `Flow` с обработкой ошибок
  - Утилиты для ввода дат

- **UI Components**
  - Кастомные View-элементы
  - `LoadingController` для управления состоянием загрузки
  - Адаптеры для `RecyclerView`

---

### 2. Doctor Application (`ru.scolio.nfc.doctor`)
Приложение для врачей с расширенным функционалом.

#### Основные экраны:
- **Authentication**
  - `LoginFragment` — вход в систему  
  - `LoginViewModel` — логика аутентификации

- **Workspace**
  - `WorkspaceFragment` — основное рабочее пространство  
  - Навигация через `BottomNavigationView`

- **Patients Management**
  - `PatientListFragment` — список пациентов с пагинацией  
  - `PatientDetailFragment` — детальная информация  
  - `PatientEditFragment` — создание и редактирование пациентов

- **Scanner Flow**
  - `SensorScannerFlowFragment` — поток сканирования  
  - `DeactivatedSensorFragment` — работа с деактивированными датчиками  
  - `UnattachedPatientFragment` — привязка датчиков к пациентам

---

### 3. Patient Application (`ru.scolio.nfc.patient`)
Упрощенное приложение для пациентов.

#### Основные экраны:
- Сканирование датчиков  
- Просмотр данных о ношении  
- График использования  

---

### 4. Persistent Layer (`ru.scolio.nfc.persistent`)
Слой работы с данными и API.

#### Репозитории:
- `PatientRepository` — управление пациентами  
- `SensorRepository` — работа с датчиками  
- `TokenRepository` — аутентификация  
- `LogRepository` — логирование действий  

#### API:
- GraphQL-клиент через **Apollo**

---

### 5. Sensor Library (`ru.scolio.nfc.sensor`)
Библиотека для работы с NFC-датчиками.

#### Основные компоненты:
- `ScolioSensorController` — основной контроллер
  - Чтение состояния датчика  
  - Получение измерений (температура)  
  - Активация / деактивация датчиков  

---

## Технологический стек

- **Kotlin** — основной язык разработки  
- **MVVM** — архитектура приложения  
- **Coroutines / Flow** — асинхронное программирование  
- **Koin** — dependency injection  
- **Apollo GraphQL** — работа с API  
- **Android Navigation Component** — навигация  
- **Material Design** — UI-компоненты  
- **MPAndroidChart** — построение графиков  
- **Firebase Crashlytics** — отслеживание ошибок  

---

## Настройка зависимостей

Проект использует модульную структуру с разделением на:
- `core` — общие компоненты  
- `doctor` — приложение для врачей  
- `patient` — приложение для пациентов  
- `persistent` — работа с данными  
- `sensor` — NFC-библиотека  

## Установка и запуск проекта
1. Запустить Android Studio
2. Открыть директорию проекта
3. Дождаться окончания индексации Gradle Sync
!Если Gradle не подгрузил зависимости автоматически — нажать File → Sync Project with Gradle Files

##  Создание apk-файла
1. Выбрать пункт "Build" -> "Generate Signed App Bundle or APK" -> "Apk"
2. Нажать на кнопку "Choose existing.." и выбрать файл ScolioNFCKeystore
3. В зависимоти от создаваемого приложения открыть файл PatientKeyStore.properties или DoctorKeystore.properties и заполнить соответсвтувющие поля из файла. Нажать "Next"
4. Выбрать "release" -> "Create" 
