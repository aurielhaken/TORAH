#!/usr/bin/env python3
"""
Script de test pour les codes Torah
Teste les différentes méthodes d'analyse
"""

from ai.codes_torah import AnalyseurCodesTorah

def test_guematrie():
    """Test de la guématrie"""
    print("\n" + "="*60)
    print("TEST: GUÉMATRIE")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    # Test 1: Amour = Un
    ahava = analyseur.calculer_guematrie("אהבה")
    ehad = analyseur.calculer_guematrie("אחד")

    print(f"\n✡️  אהבה (Ahava - Amour) = {ahava.valeur}")
    print(f"✡️  אחד (Ehad - Un) = {ehad.valeur}")

    if ahava.valeur == ehad.valeur:
        print("✅ RÉVÉLATION: L'amour et l'unité sont identiques !")
        if ahava.correspondances:
            print(f"   Correspondances: {', '.join(ahava.correspondances)}")

    # Test 2: Hashem
    hashem = analyseur.calculer_guematrie("יהוה")
    print(f"\n✡️  יהוה (Hashem - Le Nom) = {hashem.valeur}")
    if hashem.correspondances:
        print(f"   Correspondances: {', '.join(hashem.correspondances)}")

    # Test 3: Messie
    mashiah = analyseur.calculer_guematrie("משיח")
    print(f"\n✡️  משיח (Mashiah - Messie) = {mashiah.valeur}")
    if mashiah.correspondances:
        print(f"   Correspondances: {', '.join(mashiah.correspondances)}")

    # Test 4: Guématrie katan
    shalom = analyseur.calculer_guematrie("שלום", "katan")
    print(f"\n✡️  שלום (Shalom - Paix) Katan = {shalom.valeur}")


def test_atbash():
    """Test d'At-Bash"""
    print("\n" + "="*60)
    print("TEST: AT-BASH (אתב״ש)")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    # Test 1: Babel
    babel = "בבל"
    babel_atbash = analyseur.appliquer_atbash(babel)
    print(f"\n✡️  בבל (Babel) → At-Bash → {babel_atbash}")
    print("   📖 Référence: Jérémie 25:26 mentionne 'Sheshakh' (ששך)")

    # Test 2: Torah
    torah = "תורה"
    torah_atbash = analyseur.appliquer_atbash(torah)
    print(f"\n✡️  תורה (Torah) → At-Bash → {torah_atbash}")

    # Test 3: Symétrie
    test = "אמת"
    test_atbash = analyseur.appliquer_atbash(test)
    test_decode = analyseur.decoder_atbash(test_atbash)
    print(f"\n✡️  Symétrie At-Bash:")
    print(f"   Original: {test}")
    print(f"   Encodé: {test_atbash}")
    print(f"   Décodé: {test_decode}")
    print(f"   ✅ Symétrique: {test == test_decode}")


def test_notarikon():
    """Test de Notarikon"""
    print("\n" + "="*60)
    print("TEST: NOTARIKON (נוטריקון)")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    # Test 1: Acronyme Shema
    shema = analyseur.analyser_notarikon("שמע ישראל")
    print(f"\n✡️  Acronyme de 'שמע ישראל': {shema.acronyme}")

    # Test 2: Expansion Amen
    amen = analyseur.analyser_notarikon("אמן", mode="expansion")
    print(f"\n✡️  Expansion de 'אמן':")
    if amen.expansion:
        print(f"   {amen.expansion}")

    # Test 3: Rambam
    rambam = analyseur.analyser_notarikon("רמב״ם", mode="expansion")
    print(f"\n✡️  Expansion de 'רמב״ם' (Maimonide):")
    if rambam.expansion:
        print(f"   {rambam.expansion}")


def test_temourah():
    """Test de Témourah"""
    print("\n" + "="*60)
    print("TEST: TÉMOURAH (תמורה)")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    # Test 1: Rotations cycliques
    mot = "אור"
    variantes = analyseur.analyser_temourah(mot, "cyclique")
    print(f"\n✡️  Rotations cycliques de 'אור' (Lumière):")
    for i, v in enumerate(variantes, 1):
        print(f"   {i}. {v}")


def test_els():
    """Test de recherche ELS"""
    print("\n" + "="*60)
    print("TEST: ELS (Equidistant Letter Sequences)")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    # Créer un texte de test simple
    texte_test = "בראשיתבראאלהיםאתהשמיםואתהארץ" * 3  # Genèse 1:1 répété
    mot = "תורה"

    resultats = analyseur.rechercher_els(texte_test, mot, 1, 20)

    print(f"\n✡️  Recherche ELS de 'תורה' (Torah)")
    print(f"   Résultats trouvés: {len(resultats)}")

    if resultats:
        print("\n   Top 3 résultats:")
        for i, r in enumerate(resultats[:3], 1):
            print(f"   {i}. Position: {r.position_debut}, Intervalle: {r.intervalle}, Pertinence: {r.pertinence:.2f}")


def test_analyse_complete():
    """Test d'analyse complète"""
    print("\n" + "="*60)
    print("TEST: ANALYSE COMPLÈTE")
    print("="*60)

    analyseur = AnalyseurCodesTorah()

    mot = "שלום"
    print(f"\n✡️  Analyse complète de 'שלום' (Shalom - Paix)\n")

    resultats = analyseur.analyser_tout(mot)

    # Guématrie
    if resultats.get('guematrie'):
        print("   📊 GUÉMATRIE:")
        gue = resultats['guematrie']
        print(f"      Standard: {gue['standard']['valeur']}")
        print(f"      Katan: {gue['katan']['valeur']}")
        print(f"      Sidouri: {gue['sidouri']['valeur']}")

    # At-Bash
    if resultats.get('atbash'):
        print(f"\n   🔄 AT-BASH:")
        print(f"      {resultats['atbash']['texte_atbash']}")

    # Notarikon
    if resultats.get('notarikon'):
        print(f"\n   📝 NOTARIKON:")
        not_acr = resultats['notarikon']['acronyme']
        print(f"      Acronyme: {not_acr['acronyme']}")

    # Témourah
    if resultats.get('temourah'):
        print(f"\n   🔀 TÉMOURAH (Cyclique):")
        for v in resultats['temourah']['cyclique'][:3]:
            print(f"      {v}")


def main():
    """Exécute tous les tests"""
    print("\n" + "="*60)
    print("🔯 TESTS DES CODES CACHÉS DE LA TORAH 🔯")
    print("="*60)
    print("\nCes méthodes révèlent les dimensions cachées du texte sacré")
    print("Basées sur la tradition kabbalistique millénaire\n")

    test_guematrie()
    test_atbash()
    test_notarikon()
    test_temourah()
    test_els()
    test_analyse_complete()

    print("\n" + "="*60)
    print("✅ TOUS LES TESTS COMPLÉTÉS")
    print("="*60)
    print("\n📖 Références:")
    print("   - Sefer Yetzirah (Livre de la Formation)")
    print("   - Bahir (Livre de la Clarté)")
    print("   - Zohar (Livre de la Splendeur)")
    print("\n🙏 B'hatzla'ha!\n")


if __name__ == "__main__":
    main()
