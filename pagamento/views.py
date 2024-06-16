from django.shortcuts import render,HttpResponse
import requests
import json


def getPublicKey():

    url = "https://sandbox.api.assinaturas.pagseguro.com/public-keys"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "7f19e2d0-2774-44e5-8d0e-7efefe8be849557ab247436f91b32802981b2e99fd681789-cfc4-47a4-a604-7f1c542bd135"
    }

    body = json.dumps({
        "type":"carrd"
    })

    response = requests.put(url, headers=headers,data=body)

    
    return response.json()['public_key']


def home(request):     
    data = {}
    data['publickey'] = getPublicKey()
    return render(request,'index.html',data)

def pagamentos(request):

    url = 'https://sandbox.api.pagseguro.com/orders'

    headers = {
        "Content-Type": "application/json",
        "Authorization": "7f19e2d0-2774-44e5-8d0e-7efefe8be849557ab247436f91b32802981b2e99fd681789-cfc4-47a4-a604-7f1c542bd135"
    }

    body = json.dumps({
        "reference_id": "ex-00001",
        "customer": {
            "name": "Jose da Silva",
            "email": "email@test.com",
            "tax_id": "12345678909",
            "phones": [
            {
                "country": "55",
                "area": "11",
                "number": "999999999",
                "type": "MOBILE"
            }
            ]
        },
        "items": [
            {
            "reference_id": "referencia do item",
            "name": "nome do item",
            "quantity": 1,
            "unit_amount": 500
            }
        ],
        "shipping": {
            "address": {
            "street": "Avenida Brigadeiro Faria Lima",
            "number": "1384",
            "complement": "apto 12",
            "locality": "Pinheiros",
            "city": "São Paulo",
            "region_code": "SP",
            "country": "BRA",
            "postal_code": "01452002"
            }
        },
        "notification_urls": [
            "https://meusite.com/notificacoes"
        ],
        "charges": [
            {
            "reference_id": "MY-ID-123",
            "description": "Motivo de pagamento",
            "amount": {
                "value": 1000,
                "currency": "BRL"
            },
            "payment_method": {                             
                "type": "CREDIT_CARD",
                "installments": 1,
                "capture": True,
                "soft_descriptor": "Loja do meu teste",
                "card": {                    
                    "number": "4111111111111111",
                    "exp_month": "03",
                    "exp_year": "2026",
                    "security_code": "123",
                    "holder": {
                        "name": "Jose da Silva",
                        "tax_id": "65544332211"
                    },
                    "store":True
                    }
            },
            
            "notification_urls": [
                "https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-4c3f4a1fdc46/"
            ]
            }
        ]
    })

    response = requests.post(url, headers=headers,data=body)


    return HttpResponse(response)
