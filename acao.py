import yfinance

ticker = input("Digite o código da ação: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd):")
dt_final = input("Digite a data final (aaaa-mm-dd):")
dados=yfinance.Ticker(ticker)
tabela = dados.history(start=dt_inicial, end=dt_final)
tabela