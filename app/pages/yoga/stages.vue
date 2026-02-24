<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">

    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-equilibre-nobg.png"
        alt=""
        class="absolute top-1/2 left-[20%] h-[110%] w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(10%); mix-blend-mode: multiply; transform: translate(-50%, -50%);"
      />
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 flex flex-col lg:flex-row gap-10 relative z-10">
      <!-- Espace conservé pour maintenir le texte à droite -->
      <div class="hidden lg:block lg:w-80 shrink-0">
      </div>

      <!-- Contenu principal -->
      <div class="flex-1">
        <h1 class="text-5xl font-light text-stone-950 mb-8">Les Stages</h1>

        <p class="text-xl text-stone-800 leading-relaxed mb-12">
          Des stages de yoga Iyengar® pour expérimenter la pratique dans la durée.
        </p>

        <div class="space-y-6">
          <!-- Stage à venir -->
          <div class="bg-white rounded-2xl p-8 shadow-xl shadow-stone-200 border border-stone-100 border-l-4 border-l-orange-500 relative overflow-hidden group">
            <div class="relative z-10">
              <div class="inline-flex items-center gap-1.5 bg-orange-600 text-white text-xs font-bold uppercase tracking-widest px-2.5 py-1 rounded-full mb-4">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-200 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-white"></span>
                </span>
                Prochain stage
              </div>

              <h2 class="text-3xl font-semibold text-stone-950 mb-2">11 et 12 avril 2026</h2>
              <p class="text-stone-900 text-lg mb-6 leading-relaxed">
                Un week-end au Studio de Larchant pour approfondir votre pratique.<br>
                <span class="font-medium bg-stone-100 text-orange-900 px-2 py-0.5 rounded italic">Horaires : 9h30–12h30 & 15h00–17h00</span>
                <span class="font-medium bg-stone-100 text-stone-900 px-2 py-0.5 rounded italic">Tarif : 100€</span>
              </p>

              <div class="flex flex-col sm:flex-row items-center gap-4 pt-2">
                <UButton to="mailto:antonine.rochet@hotmail.fr" icon="i-heroicons-envelope" color="neutral" variant="solid" size="lg">
                  Réserver ma place
                </UButton>
                <span class="text-stone-600 text-sm">
                  ou contactez-moi : <a href="mailto:antonine.rochet@hotmail.fr" class="underline hover:text-orange-600 text-stone-900">antonine.rochet@hotmail.fr</a>
                </span>
              </div>
            </div>
          </div>

          <!-- Stage passé -->
          <div class="bg-white/50 rounded-2xl p-6 border border-stone-200/60 grayscale opacity-50 hover:opacity-80 transition-opacity mb-12">
            <div class="flex justify-between items-start">
              <div>
                <div class="inline-block bg-stone-300 text-white text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded mb-3">
                  Stage précédent
                </div>
                <h3 class="text-xl font-medium text-stone-800 mb-1">9-10 Février 2026</h3>
                <p class="text-stone-500">
                  Thème : Les Inversions — Studio de Larchant
                </p>
              </div>
            </div>
          </div>
        </div>


        <!-- Autres formules -->
        <div class="space-y-6">
          <div class="bg-white shadow-sm rounded-2xl p-6 border border-stone-200/60 relative overflow-hidden">
            <h2 class="text-2xl font-bold text-stone-950 mb-4">Stages semaine</h2>
            <p class="text-stone-800 mb-4">
              Cinq jours, cela laisse le temps d'installer une atmosphère propice à la pratique et d'ouvrir le corps avant de l'amener à des postures plus avancées.
            </p>
            <ul class="space-y-2 text-stone-800">
              <li>• Durée : 5 jours</li>
              <li>• Programme : 3h de pratique activele matin et 2h de restauratif l'après-midi</li>
              <li>• Tarif : 300€</li>
              <li>• Niveau : un an de pratique Iyengar® minimum ou 3 ans d'un autre yoga</li>
            </ul>
          </div>

          <div class="bg-white shadow-sm rounded-2xl p-6 border border-stone-200/60 relative overflow-hidden">
            <h2 class="text-2xl font-bold text-stone-950 mb-4">Stages weekend</h2>
            <p class="text-stone-800 mb-4">
              Deux jours pour explorer des postures qui demandent un long temps de préparation ainsi que le pranayama.
            </p>
            <ul class="space-y-2 text-stone-800">
              <li>• Durée : 2 jours</li>
              <li>• Programme : 3h de pratique activele matin et 2h de restauratif l'après-midi</li>
              <li>• Tarif : 100€</li>
              <li>• Niveau : un an de pratique du yoga minimum</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Stages de Yoga Iyengar à Larchant et Fontainebleau | Week-ends & Retraites',
  description: 'Stages de yoga Iyengar® en Seine-et-Marne : week-ends intensifs, retraites, ateliers thématiques. Approfondissez votre pratique à Larchant près de Fontainebleau.',
  keywords: 'stage yoga Larchant, stage yoga Fontainebleau, retraite yoga 77, week-end yoga Seine-et-Marne, stage yoga Iyengar®, atelier yoga, séjour yoga France'
})
</script>
