print("--------------YO----------------")
nombre=0
edad=0
altura=0
soyTrainner=0
pasatiempos={"Jugar", "TV"}
ropa={
    "Camiseta": "Azul",
    "Lentes": True,
    "Zapatos": "Tenis",
    "Pantalon": "Negro"
}

nombre=input("Ingrese Nombre Completo: ")
edad= input("Ingrese Edad :  ")
altura= input("Altura :")
soyTrainner= input("Eres Trainner (Si o No): ")

print("Me Llamo "+nombre,"tengo " +edad,  "Mido " +altura, "Soy Trainner? " +soyTrainner)
print("Hoy estoy vestido con camiseta:"+{ropa.get('camiseta')})




