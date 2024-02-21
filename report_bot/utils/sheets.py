from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pg_maker import all_authors
from utils.calendar import current_month
from collections import defaultdict
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SAMPLE_SPREADSHEET_ID = "14rfetnaiqgiT3o0TsLC-yi3EICobIH5rNljilhDS70M"

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())


def rep_month(month):
  SAMPLE_RANGE_NAME = f"{month}!A2:G"

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    dct = dict()

    for row in values:
      try:
        key = row[2]
        value = int(row[6])
        if key in dct:
          current_sum, current_count = dct[key]
          dct[key] = (current_sum + value, current_count + 1)
        else:
          dct[key] = (value, 1)
      except:
        pass

    msg = ''
    sorted_dct = sorted(dct.items(), key=lambda item: item[1][0], reverse=True)
    for author, summa in sorted_dct:
        msg += f"{author} — {summa[0]} руб.\nТекстов за месяц — {summa[1]}\n\n"
    return msg

  except HttpError as err:
    return str("Бот приболел. Немедленно сообщите об этом Лехе!")


def rep_name_and_month(name, month='Январь 2024'):
    SAMPLE_RANGE_NAME = f"{month}!A2:G"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        dct = dict()
        dct_texts = dict()
        for row in values:
            try:
                title = f"{row[0]} — {row[6]} руб. {row[1]}"
                money = int(row[6])
                link = row[1]
                if name == row[2]:
                    if (name in dct or name in dct_texts):
                        if link:
                            value_money, current_count = dct[name]
                            dct_texts[name].append(title)
                            dct[name] = (value_money + money, current_count + 1)
                    else:
                        dct[name] = (money, 1)
                        dct_texts[name] = [title]
            except:
                pass
        msg = ''
        sorted_dct = sorted(dct.items(), key=lambda item: item[1][0], reverse=True)
        for author, summa in sorted_dct:
            msg += f"Гонорар за {month} — {summa[0]} руб.\nТекстов за месяц — {summa[1]}\n\nВсе тексты: \n"

        msg_texts = ''
        for title in dct_texts[name]:
            msg_texts += f"\n— {title}\n"
        msg += msg_texts
        return msg

    except HttpError as err:
        print(err)
        return str("Что-то неправильно вводишь!")


def who_is_free():
    SAMPLE_RANGE_NAME = f"{current_month()}!A2:C"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        all_nicknames = [(i[1], i[2]) for i in all_authors()]
        for row in values:
            try:
                author = str(row[2])
                link = row[1]
                if author and not link:
                    for nickname_tuple in all_nicknames:
                        if author in nickname_tuple:
                            all_nicknames.remove(nickname_tuple)
            except:
                pass

        return all_nicknames

    except HttpError as err:
        print(err)
        return str("Бот приболел. Немедленно сообщите об этом Лехе!")





def brief_is_free():
    SAMPLE_RANGE_NAME = f"{current_month()}!A2:J"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        all_briefs = []
        for row in values:
            try:
                title = str(row[0])
                brief = str(row[3])
                author = row[2]
                money = str(row[6])
                symbs = str(row[8])
                if brief and not author:
                    temp_row = f'[{title}]({brief})\n' \
                               f'Объем: {symbs} тыс. символов\n' \
                               f'Гонорар: {money}\n\n'
                    all_briefs.append(temp_row)
            except:
                pass

        msg = ''
        for num, brief in enumerate(all_briefs, start=1):
            msg += f"{num}. {brief}"

        return msg

    except HttpError as err:
        print(err)
        return str("Бот приболел. Немедленно сообщите об этом Лехе!")


def stats_for_month(month):
    SAMPLE_RANGE_NAME = f"{month}!A2:G"
    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        done, in_work, all_texts, seo, simple, review, test = 0, 0, 0, 0, 0, 0, 0
        for row in values:
            try:
                title = row[0]
                link = row[1]
                brief = row[3]
                type = row[5]

                seo += 1 if type == 'СЕО' else 0
                simple += 1 if type == 'Простая' or row[5] == 'Новость' else 0
                review += 1 if type == 'Обзор' else 0
                test += 1 if type == 'Тест' else 0

                if title and brief:
                    all_texts += 1

                    if link:
                        done += 1
                    else:
                        in_work += 1
            except:
                pass

        msg = f'Всего текстов за месяц: {all_texts}\n' \
              f'Уже готовы: {done}\n' \
              f'Сейчас в работе: {in_work}\n\n' \
              f'Простых — {simple} шт\n' \
              f'СЕО — {seo} шт\n' \
              f'Тестов — {test}\n' \
              f'Обзоров — {review}\n'
        return msg

    except HttpError as err:
        print(err)
        return str("Что-то неправильно ввели. Делайте нормально!")



