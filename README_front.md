# Scoliologic

## Структура проекта

```
src/
├── components/
│   ├── shared/           
│   │   ├── Header.vue       
│   │   └── VHeader.vue     
│   └── views/            
│       ├── AuthPage.vue           
│       ├── DoctorCreate.vue       
│       ├── DoctorList.vue         
│       ├── DoctorProfile.vue      
│       ├── LogPage.vue            
│       ├── NotFoundPage.vue       
│       ├── PasswordChange.vue     
│       ├── PatientCreate.vue      
│       ├── PatientGraph.vue       
│       ├── PatientProfile.vue     
│       └── PatientList.vue        
├── routers.js            
├── main.js               
└── scss/                 
    ├── base/             
    ├── components/       
    ├── utils/            
    └── vendors/          
```

---

## Ролевая модель

### Администратор
- Просмотр и управление всеми врачами  
- Создание новых врачей  
- Блокировка/разблокировка аккаунтов врачей
- Выбор привилегии по просмотру всех/своих пациентов
- Выбор привелегии доступа к 3D приложению 
- Просмотр логов  
- Смена паролей врачей 

### Врач
- Просмотр и управление своими пациентами  
- Создание новых пациентов  
- Просмотр графиков ношения медицинских устройств  
- Редактирование профилей пациентов  

---

## Интерфейс

### Компоненты интерфейса
- Модальные окна  
- Виртуальный скроллинг 
- Адаптивный дизайн
- Валидация форм
- Графики  

### Стилизация
- **Material Design Icons** — иконки  
- **SCSS переменные** — централизованное управление стилями  

---


## Установка

1. Склонировать репозиторий
1. Запустить `yarn`

## Использование

### Development

```bash
yarn serve
```

### Build

```bash
yarn build
```
После выполнения build в корне каталога будет создан stats.html для визуализации бандла проекта

### Scripts
Остальные скрипты описаны в package.json

## Особенности

-   ⚡️ [Vue 3](https://github.com/vuejs/vue-next), [Vite 2](https://github.com/vitejs/vite)

-   😃 [Material Icons Font](https://fonts.google.com/icons)

-   🐺 [Stylelint](https://stylelint.io/), [ESLint](https://eslint.org/) c использованием [Husky](https://github.com/typicode/husky)

-   👀 [Rollup-plugin-visualizer](https://www.npmjs.com/package/rollup-plugin-visualizer)

-   🚩 [Postcss](https://postcss.org/) c использованием [autoprefixer](https://github.com/postcss/autoprefixer), [cssnano](https://cssnano.co/docs/getting-started/) и [purgecss](https://purgecss.com/plugins/postcss.html)

## Рекомендации

-   ✏️ [VSCode](https://code.visualstudio.com/) + VSCode ESLint, Stylelint плагины




