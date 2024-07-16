from datetime import datetime, timezone, timedelta

#CRIANDO DATETIME COM TIMEZONE
d = datetime.now(timezone(timedelta(hours=-3), "BRT"))
data_oslo = datetime.now(timezone(timedelta(hours=2)))
print(d)
print(data_oslo)

d_utc = d.astimezone(timezone.utc)
print(d_utc)
