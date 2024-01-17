[![Nginx](https://img.shields.io/badge/Nginx-Latest-blue?style=flat&logo=nginx&logoColor=white)](https://nginx.org/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
-----
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.3.0-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/Pydantic/2.3.0/)
[![Django](https://img.shields.io/badge/Django-5.0.1-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/Django/)
[![Openpyxl](https://img.shields.io/badge/Openpyxl-3.1.2-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/openpyxl/)
---
[![Poetry](https://img.shields.io/badge/Poetry-used-green?style=flat&logo=python&logoColor=white)](https://pypi.org/project/poetry/)
[![Ruff](https://img.shields.io/badge/Ruff-used-green?style=flat&logo=python&logoColor=white)](https://pypi.org/project/ruff/)

# Test-case-RusGidro

### Сервис, проверяющий корректность исчисления НДФЛ сотрудникам.

На главной станице приложения выберите файл и нажмите кнопку загрузить. 
Пример шаблона проверяемых данных и отчёта представлен в папке Task description.
После загрузки файла появится ссылка на отчёт. При нажатии, Вам предложат скачать файл с отчётом, сформированном по следующему описанию:

Отчет содержит следующие столбцы:  
  1. Филиал (из исходных данных);  
  2. Сотрудник (из исходных данных);  
  3. Налоговая база (из исходных данных);  
  4. Исчислено всего (из исходных данных);  
  5. Исчислено всего по формуле (новый столбец);  
  6. Отклонения (новый столбец) – если отклонений нет, то фон ячеек зеленый, иначе – красный  
Формула новых столбцов:  
  1. Исчислено всего по формуле – если «Налоговая база» <= 5000000, то «Налоговая база» * 13%, величина превышения 5000000 облагается по ставке 15%;  
  2. Отклонения (новый столбец) – «Исчислено всего» - «Исчислено всего по формуле»;  
Отчет отсортирован по убыванию по столбцу «Отклонения».

Как установить и запустить приложение:

### Установка и запуск проекта

Клонировать репозиторий и перейти в него в командной строке:
```bash
git@github.com:MultikPatin/Test-case-RusGidro.git
```
Перейти в него в командной строке:

```bash
cd Test-case-RusGidro
```
Установить менеджер зависимостей poetry
```bash
python -m pip install poetry
```
Флаг для создания файлов виртуального окружения в корне репозитория
```bash
poetry config virtualenvs.in-project true
```
Установка пакета зависимостей без библиотек для разработки
```bash
poetry install --without dev
```
Проект запускается в 2 контейнерах

- nginx
- nalog_app
  
Необходимые инструменты для запуска

Docker

Перед запуском необходимо создать файл .env с переменными в 
корневом каталоге. Пример в файле .env.exemple

 - SECRET_KEY
 - ALLOWED_HOSTS
 - DEBUG

#### Запуск контейнеров

 В корневом каталоге выполнить каманду

```bash
docker-compose up -d
```




