# Scolio NFC

**Scolio NFC** — мобильное приложение для работы с NFC-датчиками мониторинга осанки.  
Проект реализует две версии приложения — для врачей и пациентов, а также предоставляет отдельную библиотеку для взаимодействия с NFC-датчиками.

---

## Архитектура проекта

Проект состоит из нескольких модулей, каждый из которых выполняет свою роль:

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
  - Поддержка сетевых и аутентификационных ошибок

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
- Графики использования  

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
- Конфигурация для разных окружений (`dev`, `prod`)
- Маппинг данных между API и доменной моделью

---

### 5. Sensor Library (`ru.scolio.nfc.sensor`)
Библиотека для работы с NFC-датчиками.

#### Основные компоненты:
- `ScolioSensorController` — основной контроллер
  - Чтение состояния датчика  
  - Получение измерений (температура, напряжение)  
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

## Структура данных

### Patient
```kotlin
data class Patient(
    val id: PatientId,
    val firstName: String,
    val secondName: String,
    val surName: String?,
    val birthDate: Date,
    val recommendedTime: Double?,
    val comment: String?,
    val doctorId: DoctorId,
    val isSensor: Boolean
)
```

### Sensor
```kotlin
data class Sensor(
    val serialNumber: SensorSerial,
    val id: SensorId,
    val patientId: PatientId?
)
```

### SensorValue
```kotlin
data class SensorValue(
    val date: Date,
    val useTime: Double
)
```

---

## Настройка зависимостей

Проект использует модульную структуру с разделением на:
- `core` — общие компоненты  
- `doctor` — приложение для врачей  
- `patient` — приложение для пациентов  
- `persistent` — работа с данными  
- `sensor` — NFC-библиотека  

---

## Особенности реализации

### Обработка ошибок
Композитная система обработчиков позволяет последовательно обрабатывать ошибки разными обработчиками.

### Состояние загрузки
Унифицированный `LoadingController` используется для отображения и управления состояниями загрузки.

### Пагинация
Реализована с помощью **Paging 3** для эффективной работы со списками.

### NFC-взаимодействие
Библиотека предоставляет полный контроль над NFC-датчиками: чтение, активация, калибровка.

---

## Конфигурация сборки

Поддерживаются окружения:
- **Development**
- **Production**
- **Production Scolio**

Пример конфигурации:
```kotlin
when (BuildConfig.SERVER) {
    "dev" -> ApiConfiguration.devServerUrl
    "prod" -> ApiConfiguration.prodServerUrl
    "prodScolio" -> ApiConfiguration.prodScolioServerUrl
}
```

---

## Безопасность

- Используется **Basic Authentication** для API  
- Токены хранятся в **Secure SharedPreferences**  
- Реализована валидация входных данных  
- Обрабатываются ошибки аутентификации  

---

## Лицензия

Проект предназначен для внутреннего использования и не распространяется публично.
