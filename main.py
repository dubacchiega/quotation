import requests

class CurrenceConvertor:
    def __init__(self, coin:str) -> None:
        self.coin = coin.upper()


    def finalResponse(self):
        self.response = requests.get(f'https://economia.awesomeapi.com.br/last/{self.coin}-BRL')
        self.response = self.response.json()
        if 'status' in self.response:
            if self.response['status'] == 404:
                return 'Moeda não encontrada'
        else:
            self.bid_response = self.response[f'{currency}BRL']["bid"]
            self.name = self.response[f'{currency}BRL']['name']
            return f'Moeda: {self.name} ----- cotação: {round(float(self.bid_response), 2)}'
        
    def currenceExchange(self, value):
        try:
            value = float(value)
            self.value = value
            self.resp = self.value * float(self.bid_response)
            name_currency = self.name.split('/')
            return f'O valor de {self.value} convertido de {name_currency[0]} para {name_currency[1]} é: {round(self.resp, 2)}'
        except (ValueError, AttributeError):
            return 'Digite apenas números'


if __name__ == '__main__':
    currency = input('Digite o prefixo da moeda. (EXEMPLO: USD, EUR): ').upper()
    value_input = input('Digite o valor que você deseja converter: ')
    moeda = CurrenceConvertor(currency)
    print(moeda.finalResponse())
    print()
    print(moeda.currenceExchange(value_input))