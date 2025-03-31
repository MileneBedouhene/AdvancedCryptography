def RailcipherText(clearText, key):
    if key <= 1:
        return clearText  # Pas de transformation si key == 1

    result = ""
    matrix = [["" for _ in range(len(clearText))] for _ in range(key)]

    row, col, direction = 0, 0, 1

    # Placer les caractères dans la matrice
    for c in clearText:
        matrix[row][col] = c
        col += 1
        row += direction

        # Inverser la direction si on atteint un bord
        if row == 0 or row == key - 1:
            direction *= -1

    # Lire la matrice rail par rail
    for rail in matrix:
        result += "".join(rail)

    return result


def RaildecipherText(cipherText, key):
    if key <= 1:
        return cipherText  # Pas de transformation si key == 1

    # Créer une matrice vide
    matrix = [["" for _ in range(len(cipherText))] for _ in range(key)]
    
    # Marquer les positions des lettres
    row, direction = 0, 1
    for col in range(len(cipherText)):
        matrix[row][col] = "*"
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    # Remplir la matrice avec le texte chiffré
    idx = 0
    for r in range(key):
        for c in range(len(cipherText)):
            if matrix[r][c] == "*" and idx < len(cipherText):
                matrix[r][c] = cipherText[idx]
                idx += 1

    # Lire la matrice en suivant le motif en zigzag
    result = ""
    row, direction = 0, 1
    for col in range(len(cipherText)):
        result += matrix[row][col]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return result


# 🔹 Test du chiffrement et déchiffrement
message = "HELLO RAILFENCE"
key = 3

encrypted = RailcipherText(message, key)
decrypted = RaildecipherText(encrypted, key)

print(f"Texte original  : {message}")
print(f"Texte chiffré   : {encrypted}")
print(f"Texte déchiffré : {decrypted}")
