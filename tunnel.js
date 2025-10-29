#!/usr/bin/env node
const localtunnel = require('localtunnel');

console.log('🕎 Torah AI - Création du tunnel public...');
console.log('='.repeat(60));

(async () => {
  try {
    const tunnel = await localtunnel({ port: 8000 });

    console.log('\n✅ Tunnel créé avec succès !');
    console.log('='.repeat(60));
    console.log('\n📱 ACCÉDEZ À L\'APPLICATION DEPUIS VOTRE TÉLÉPHONE :');
    console.log(`\n   ${tunnel.url}`);
    console.log(`\n📚 Documentation interactive :`);
    console.log(`   ${tunnel.url}/docs`);
    console.log(`\n🏠 Page d'accueil :`);
    console.log(`   ${tunnel.url}/`);
    console.log('\n' + '='.repeat(60));
    console.log('📌 GARDEZ CETTE FENÊTRE OUVERTE');
    console.log('   Le tunnel restera actif tant que ce script tourne');
    console.log('   Appuyez sur Ctrl+C pour arrêter le tunnel');
    console.log('='.repeat(60));

    tunnel.on('close', () => {
      console.log('\n🛑 Tunnel fermé.');
      process.exit(0);
    });

    // Garder le processus actif
    process.stdin.resume();

  } catch (err) {
    console.error('❌ Erreur:', err.message);
    process.exit(1);
  }
})();
