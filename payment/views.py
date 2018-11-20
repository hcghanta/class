import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.core.mail import EmailMessage
from twilio.rest import Client

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({ 'amount': '{:.2f}'.format(order.get_total_cost()), 'payment_method_nonce': nonce, 'options': { 'submit_for_settlement': True } })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            subject = 'UNOSocial Payment Receipt - Invoice no. {}'.format(order.id)
            messages = 'Hello, this is a confirmation email to inform your payment is sucessfully processed. Thank you for shopping at UNOSocial! '
            email = EmailMessage(subject,
                                 messages,
                                 'admin@carlot.com',
                                 [order.email])
            email.send()

            account_sid = 'ACcb9a224f2c35facd6436041fdb3ea082'
            auth_token = '97713cb9cf222e0a17731e078657ea90'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body="Order Successsfully placed",
                from_='+15313018715',
                to='+14023058152'
            )

            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})

def payment_done(request):
    return render(request, 'payment/done.html')
	
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

