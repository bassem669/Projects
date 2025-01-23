from django.shortcuts import render

# Create your views here.
def index(request) : 
    return render(request,'index.html')


from django.shortcuts import render

def resultat(request):
    resultat : str = ''
    if request.method == "POST":
        resultat = request.POST["resultat"]
        if resultat:
            try : 
                # eval : return str
                resultat = f"{resultat} = {eval(resultat)}"
            except Exception as e :
                resultat = f"Erreur de calcul !! input no valid {e}"
        else:
            resultat = "Veuillez entrer quelque chose."
    return render(request, "index.html", {"resultat": resultat})
