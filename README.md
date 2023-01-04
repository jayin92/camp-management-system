# Camp Management System

NYCU Intro. to Database Final Project - 營隊報名審核系統

> Note: 此 repo 為公開版本，已去除個人相關資訊。

## 功能
- 從 Google 表單回覆匯入資料
- 支援帳號管理，具有審核權限的使用者可以審核報名者資料
- 支援模糊搜尋及排序
- (TODO)
- 收到匯款後可以從系統勾選並自動寄出信件，也可以直接從網站上查詢是否收到匯款
- 彙整各個審核者的評分，產生正備取名單，並自動寄出信件

## Run on local

需要先在 `camp_management_system/settings.py` 設定 Database 的連線位置。也需要將 Google 表單的資料匯出為 csv 檔案，並存於 `scripts/applicant_data.csv` 中。

在 `frontend/nuxt.config.ts` 中也要正確的設定好後端的位置。

### Backend
```bash
poetry install
poetry shell
python manage.py runserver
```

### Frontend
```bash
yarn install
yarn dev
```

## Backend
Django + Django REST Framework

## Frontend

Nuxt + Vuetify