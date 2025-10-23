# 📱 Scolio NFC

Мобильное приложение для **iOS/iPadOS** с поддержкой **NFC (ISO15693)**, предназначенное для работы с медицинскими датчиками и управления данными пациентов.  
Проект включает **два отдельных таргета** — для врачей и пациентов, а также модульную архитектуру с использованием **Swift Package Manager**.

---

## 🧩 Общее описание проекта

### Назначение
**Scolio NFC** — это система из двух мобильных приложений:

- **DoctorApplication** — приложение для врачей:
  - управление пациентами (CRUD);
  - чтение/загрузка данных с NFC-датчиков;
  - просмотр графиков показаний и состояния сенсоров.

- **PatientApplication** — приложение для пациентов:
  - просмотр собственных данных и графиков;
  - взаимодействие с NFC-сенсором (ISO15693);
  - синхронизация с сервером через GraphQL API.

---

## ⚙️ Архитектура

Проект использует **модульную архитектуру** с четким разделением ответственности:

| Модуль | Назначение |
|--------|-------------|
| **Core** | Общие утилиты, менеджеры, интерсепторы, UI-компоненты, обработка ошибок |
| **Persistent** | Слой данных, репозитории, GraphQL/Apollo-интеграция |
| **ScolioAPI** | Сгенерированные сущности GraphQL на основе схемы |
| **DoctorApplication** | Приложение для врачей (DI, презентационный слой) |
| **PatientApplication** | Приложение для пациентов (DI, презентационный слой) |

---

## 🧠 Технологии

- **Язык:** Swift 5.x  
- **UI:** SwiftUI  
- **DI и реактивность:** Combine  
- **Сеть:** Apollo iOS (GraphQL)  
- **NFC:** CoreNFC (ISO15693)  
- **Менеджер зависимостей:** Swift Package Manager (SPM)  
- **Генерация ресурсов:** SwiftGen  
- **Генерация GraphQL моделей:** Apollo iOS Codegen

---

## 📱 Минимальные требования

| Компонент | Версия |
|------------|---------|
| **iOS Deployment Target** | ≥ 14.0 *(возможна поддержка 15+ для некоторых API)* |
| **Xcode** | 14.x / 15.x |
| **Swift** | 5.9 / 5.10 |
| **Apollo iOS** | 1.22 |
| **SwiftGen** 
| **Поддерживаемые устройства** | iPhone (с NFC ISO15693) |

---

## 🧰 Структура проекта

---

### Configuration
Содержит настройки окружений и сборок:

| Файл | Назначение |
|------|-------------|
| `BuildConfiguration.swift` | Определение окружений, флагов сборки |
| `common.xcconfig` | Общие параметры сборки |
| `dev_debug.xcconfig` / `dev_release.xcconfig` | Конфигурации Development |
| `prod_debug.xcconfig` / `prod_release.xcconfig` | Конфигурации Production |

---

### Core (Swift Package)
Общий модуль инфраструктуры, включающий:

- **AccountManager** — управление аккаунтом пользователя;  
- **ErrorHandler** — централизованная обработка ошибок и сообщений;  
- **Interceptor** — интерсепторы Apollo (авторизация, логирование, токены);  
- **Networking** — базовая сеть (Endpoint, Networker, NetworkError);  
- **TagObserver** — управление NFC-тегами (BaseTagObserver, ScolioTagObserver);  
- **UI/Extensions** — кастомные SwiftUI-компоненты, стили, модификаторы;  
- **Tests/CoreTests** — модульные тесты пакета.

---

### Persistent (Swift Package)
Слой данных с GraphQL-репозиториями и маппингами:

- **API** — конфигурация ApolloClient и Combine-адаптеры;
- **Repository** — реализация репозиториев (пациенты, сенсоры, токены);
- **Model** — DTO и идентификаторы доменных сущностей;
- **Mapping** — преобразование GraphQL-моделей в доменные;
- **Tests/PersistentTests** — тесты слоя данных.

---

### ScolioAPI (Swift Package)
Содержит **сгенерированные GraphQL сущности**, основанные на схеме:
- `Fragments`, `Queries`, `Mutations`, `Schema`.
- Генерируется из GraphQL-схемы через **ScolioAPICodegen**.

---

### DoctorApplication
Таргет приложения для врачей:
- DI-композиция модулей (`DoctorApplication.swift`, `RepositoriesModule.swift`, `ServiceModule.swift`);
- Экран логина, список и детали пациентов, графики, NFC-сканер;
- Управление пациентами и датчиками;
- SwiftUI-интерфейс и Combine-вьюмодели.

---

### PatientApplication
Таргет приложения для пациентов:
- DI-композиция (`PatientApplication.swift`);
- Отображение собственных показаний и графиков;
- NFC-сканирование сенсора;
- Навигация и пагинация данных.

---

### ISO15693Tag
Обертка над **CoreNFC** для работы с ISO15693-тегами:
- подключение, чтение, запись, обработка ошибок.

---

### SharedCore
Общие компоненты UI:
- `LoadingView` — индикатор загрузки;
- `ToastView`, `ToastViewModel`, `ToastConfigurator` — уведомления.

---

### Resources
- `Assets.xcassets` — иконки, цвета, изображения;
- `Localizable.strings` — локализации (`en`, `es`, `ru`);
- `Generated` — автогенерированные Swift-файлы (SwiftGen).

---

### ScolioAPICodegen
Утилита для генерации GraphQL-моделей:
- схема (`schema.graphqls`);
- запросы/мутации (`Queries/*.graphql`);
- скрипт `Codegen.swift` для запуска Apollo Codegen.

---

### Прочее
- `swiftgen.yml` — конфигурация SwiftGen;  
- `apollo-ios-cli/` — локальный бинарь Apollo CLI;  
- `Scolio NFC.xcodeproj` и `Scolio NFC.xcworkspace` — проект и воркспейс Xcode;  
- `Scolio-NFC-Info.plist` — общие настройки и разрешения (в т.ч. NFC).

---

## 🌐 Локализация
Поддерживаются языки:
- 🇬🇧 English  
- 🇪🇸 Español  
- 🇷🇺 Русский  

---

## 🧪 CI/CD
На момент описания в проекте отсутствует CI/CD,  
но присутствуют конфигурации сборки (`xcconfig`) для окружений **dev/prod** и **debug/release**.

---

## 📈 Структура зависимостей (SPM)
| Модуль | Зависит от |
|--------|-------------|
| **DoctorApplication** | Core, Persistent, ScolioAPI |
| **PatientApplication** | Core, Persistent, ScolioAPI |
| **Persistent** | Core, Apollo iOS |
| **ScolioAPI** | Apollo iOS |
| **Core** | SwiftUI, Combine |

---

## 🚀 Быстрый старт

```bash
# Установите зависимости
swift package resolve

# Сгенерируйте ресурсы
swiftgen config run

# Сгенерируйте GraphQL модели
cd ScolioAPICodegen
swift run Codegen

# Откройте проект
open "Scolio NFC.xcworkspace"
```

### Работа с API и кодогенерация (Apollo GraphQL)

- **Apollo iOS** — используется для типобезопасной работы с GraphQL API.  
  - Запросы, мутации и схемы генерируются автоматически с помощью [Apollo Codegen](https://www.apollographql.com/docs/ios/code-generation/).
  - Файл схемы (`schema.graphqls` или `schema.json`) и определения запросов (`*.graphql`) размещаются в проекте.
  - Кодогенерация позволяет получать удобные Swift-типы, соответствующие структуре GraphQL-ответов, и использовать их напрямую в приложении без ручного парсинга.
  - что бы запустить проект надо убеиться что бы nfclibrary был в одной папке что и scoliologic-nfc-ios. В xcode выбрать одну из scheme: DeoctorApplicationProd или PatientApplicationProd.
  - если изменились запросы к бэку, в терминале запустить команду  cd <путь_к _проекту>/ScolioAPICodegen && swift run Codegen
  - в случае возникновения ошибок исправить запросы, они находятся по пути <project_root>/ScolioAPICodegen/Sources/GraphQL/
  - настройка кодогенерации находится по пути: 
<project_root>/ScolioAPICodegen/Sources/Codegen/Codegen.swift
