#!/usr/bin/env python3
"""
Démo interactive des codes Torah - Sans serveur
Utilisable directement depuis la ligne de commande
"""

from ai.codes_torah import AnalyseurCodesTorah

def demo_interactive():
    """Démo interactive"""
    analyseur = AnalyseurCodesTorah()

    print("\n" + "="*70)
    print("🔯 DÉMO INTERACTIVE - CODES TORAH 🔯")
    print("="*70)

    while True:
        print("\n📖 QUE VOULEZ-VOUS ANALYSER ?")
        print("   1. Guématrie (valeur numérique)")
        print("   2. At-Bash (substitution)")
        print("   3. Notarikon (acronyme)")
        print("   4. Analyse complète")
        print("   5. Exemples célèbres")
        print("   0. Quitter")

        choix = input("\n➤ Votre choix : ").strip()

        if choix == "0":
            print("\n🙏 Shalom ! B'hatzla'ha !")
            break

        elif choix == "1":
            texte = input("\n✡️  Entrez un mot en hébreu (ou 'test' pour אהבה) : ").strip()
            if texte == "test":
                texte = "אהבה"

            result = analyseur.calculer_guematrie(texte)
            print(f"\n📊 GUÉMATRIE de '{texte}'")
            print(f"   Valeur : {result.valeur}")
            if result.correspondances:
                print(f"   Correspondances : {', '.join(result.correspondances)}")

        elif choix == "2":
            texte = input("\n✡️  Entrez un mot en hébreu (ou 'test' pour בבל) : ").strip()
            if texte == "test":
                texte = "בבל"

            result = analyseur.appliquer_atbash(texte)
            print(f"\n🔄 AT-BASH de '{texte}'")
            print(f"   Résultat : {result}")
            if texte == "בבל":
                print(f"   📖 Référence biblique : Jérémie 25:26 (ששך)")

        elif choix == "3":
            texte = input("\n✡️  Entrez un texte (ou 'test' pour 'שמע ישראל') : ").strip()
            if texte == "test":
                texte = "שמע ישראל"

            result = analyseur.analyser_notarikon(texte)
            print(f"\n📝 NOTARIKON de '{texte}'")
            print(f"   Acronyme : {result.acronyme}")
            if result.expansion:
                print(f"   Expansion : {result.expansion}")

        elif choix == "4":
            texte = input("\n✡️  Entrez un mot (ou 'test' pour שלום) : ").strip()
            if texte == "test":
                texte = "שלום"

            resultats = analyseur.analyser_tout(texte)
            print(f"\n🔍 ANALYSE COMPLÈTE de '{texte}'")

            if resultats.get('guematrie'):
                print(f"\n   📊 Guématrie Standard : {resultats['guematrie']['standard']['valeur']}")
                print(f"      Guématrie Katan   : {resultats['guematrie']['katan']['valeur']}")

            if resultats.get('atbash'):
                print(f"\n   🔄 At-Bash : {resultats['atbash']['texte_atbash']}")

            if resultats.get('temourah'):
                print(f"\n   🔀 Témourah (3 premières rotations) :")
                for v in resultats['temourah']['cyclique'][:3]:
                    print(f"      • {v}")

        elif choix == "5":
            print("\n✨ DÉCOUVERTES CÉLÈBRES")
            print("\n   1. אהבה (Ahava - Amour) = 13")
            print("      אחד (Ehad - Un) = 13")
            print("      → L'amour et l'unité sont identiques !")

            print("\n   2. יהוה (Hashem - Le Nom) = 26")
            print("      26 = 2 × 13 (Ahava × 2)")
            print("      → Dieu est amour multiplié")

            print("\n   3. משיח (Mashiah - Messie) = 358")
            print("      נחש (Nahash - Serpent) = 358")
            print("      → Le Messie transformera le mal en bien")

            print("\n   4. בבל (Babel) → At-Bash → ששך")
            print("      → Mentionné dans Jérémie 25:26 !")

            print("\n   5. אור (Or - Lumière) → Rotation → ראו (Voyez)")
            print("      → La lumière permet de voir")

        else:
            print("\n❌ Choix invalide")

if __name__ == "__main__":
    demo_interactive()
