from firebase import firebase

firebase = firebase.FirebaseApplication('https://iteration-1-demo.firebaseio.com/')

result = firebase.get('/1Ga1RxErjr9PRtH1UnTxMOHiSF4Ff30iBAc4vB_0IaC8', None)

print(result)