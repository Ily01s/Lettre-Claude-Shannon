import correction_err  # Assurez-vous que ce module est importé correctement
import deciffreur      # Assurez-vous que ce module est importé correctement

def test():
    test_data = [0, 0, 1, 0, 0, 0, 0] * 3  # Assurez-vous que c'est un multiple complet de 7
    expected_corrected = [0, 0, 0, 0] * 3  # Attendu pour chaque bloc de 7 bits, réduit à 4 bits

    # Test avec le script original
    corrected_original = deciffreur.corriger_erreurs(test_data)
    reduced_original = deciffreur.reduire_encodage(corrected_original)

    # Test avec le nouveau script
    corrected_new = correction_err.correct_errors(test_data)
    # Assumant que la réduction est déjà incluse dans correct_errors

    print("Original script output:", reduced_original)
    print("New script output:", corrected_new)

    assert reduced_original == expected_corrected, f"Original script failed: expected {expected_corrected}, got {reduced_original}"
    assert corrected_new == expected_corrected, f"New script failed: expected {expected_corrected}, got {corrected_new}"

    print("Both scripts produce the same output for the input tested. Test passed.")

test()
