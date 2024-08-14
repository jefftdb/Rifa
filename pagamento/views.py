from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from rifa.models import Rifa, Number
import requests
import json
from datetime import datetime,timedelta,timezone

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
                "soft_descriptor": "Site de rifa",
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

def pagar_com_pix(request,rifa_id,num_id):
    agora = datetime.now(timezone.utc)
    data_expiracao = agora + timedelta(minutes=30)

    rifa = get_object_or_404(Rifa, id=rifa_id)
    numero = get_object_or_404(Number, id=num_id)

    url = "https://sandbox.api.pagseguro.com/orders"

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
            "name": f'numero:{numero} da Rifa: {rifa.title}',
            "quantity": 1,
            "unit_amount": 1
        }
    ],
    "qr_codes": [
        {
            "amount": {
                "value": int(rifa.value)  # Garantindo valor numérico
            },
            "expiration_date": data_expiracao.isoformat(),
        }
    ],
         
    "shipping": {
        "address": {
            "street": "Júlio Lopes",
            "number": "225",
            "complement": "casa 1",
            "locality": "Santa Rita",
            "city": "Mendes",
            "region_code": "RJ",
            "country": "BRA",
            "postal_code": "26700000"  # Sem hífen, apenas 8 dígitos
        }
    },
    "notification_urls": [
        "https://meusite.com/notificacoes"
    ],
})

    response = requests.post(url, headers=headers, data=body)
    response_data = response.json()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'rifa': rifa.title,
            'QR_img': response_data['qr_codes'][0]['links'][0]['href'],
            'texto_pix': response_data['qr_codes'][0]['text'],
            'order_id': response_data['id'],
            'customer_name': response_data['customer']['name'],
            'customer_email': response_data['customer']['email'],
            'customer_tax_id': response_data['customer']['tax_id'],
            'customer_phone': response_data['customer']['phones'][0]['number'],
            'item_name': response_data['items'][0]['name'],
            'item_quantity': response_data['items'][0]['quantity'],
            'item_amount': response_data['items'][0]['unit_amount'],
        })

    return render(request, 'rifa.html', context={
        'rifa': rifa,
        'QR_img': response_data['qr_codes'][0]['links'][0]['href'],
        'texto_pix': response_data['qr_codes'][0]['text'],
        'order_id': response_data['id'],
        'customer_name': response_data['customer']['name'],
        'customer_email': response_data['customer']['email'],
        'customer_tax_id': response_data['customer']['tax_id'],
        'customer_phone': response_data['customer']['phones'][0]['number'],
        'item_name': response_data['items'][0]['name'],
        'item_quantity': response_data['items'][0]['quantity'],
        'item_amount': response_data['items'][0]['unit_amount'],
    })