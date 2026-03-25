<template>
  <div class="relative min-h-screen bg-linear-to-br from-blue-50 to-stone-50 overflow-hidden">
    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-amm-nobg.png"
        alt=""
        class="absolute top-[55%] left-1/2 h-full w-auto object-contain"
        style="opacity: 0.15; filter: grayscale(10%) sepia(5%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(5deg);"
      />
    </div>

    <!-- Hero Image Full Width -->
    <div class="relative w-full aspect-[16/9] md:aspect-[3/1] overflow-hidden border-b border-white/20 shadow-lg bg-stone-100">
      <NuxtImg
        src="/images/mountain12.jpg"
        alt="Sorties en montagne - Massif de Belledonne"
        class="w-full h-full object-cover"
      />
      <!-- Very Restricted Sky smoothing overlay (Top 20% only) -->
      <div class="absolute top-0 left-0 w-full h-[20%] bg-linear-to-b from-sky-600/50 via-sky-500/20 to-transparent pointer-events-none"></div>
      
      <div class="absolute inset-0 bg-linear-to-b from-black/40 via-transparent to-stone-900/60 pointer-events-none"></div>
      <div class="absolute inset-0 flex flex-col items-center justify-center text-center p-6">
        <h1 class="text-5xl md:text-7xl font-light text-white italic drop-shadow-2xl mb-2">Les Sorties</h1>
        <p class="text-lg md:text-xl text-white/90 font-light tracking-[0.3em] uppercase">En Montagne</p>
      </div>
    </div>

    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 pb-0">
      <div class="max-w-4xl mx-auto text-center mb-24">
        <h2 class="text-3xl md:text-4xl font-light text-gray-950 italic mb-8">Explorez la nature</h2>
        <p class="text-xl md:text-2xl text-gray-700 leading-relaxed font-light mb-8">
          Accompagnatrice en montagne diplômée, je vous propose des sorties adaptées à tous les niveaux dans les
          plus beaux massifs pour allier découverte, effort et contemplation.
        </p>
        <p class="text-lg text-gray-600 leading-relaxed">
          Des randonnées d'une journée aux séjours de plusieurs jours, trail, yoga, randonnée ou tout à la fois, découvrez la montagne en toute sécurité.
        </p>
        <div class="w-16 h-1 bg-blue-500/30 mx-auto rounded-full mt-12"></div>
      </div>
      <!-- Sorties Fontainebleau -->
      <section class="mt-24 border-t border-blue-100 pt-20">
        <div class="text-center mb-16 px-4">
          <h2 class="text-4xl md:text-5xl font-light text-gray-900 mb-6 italic">Sorties en Forêt de Fontainebleau</h2>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto font-light">Zigzaguer entre chaos rocheux et étendues de sables à l'ombre des pins</p>
          <div class="w-24 h-1 bg-blue-500/30 mx-auto rounded-full mt-8"></div>
        </div>

        <div class="bg-white/40 backdrop-blur-md rounded-3xl overflow-hidden border border-white/60 shadow-2xl max-w-6xl mx-auto">
          <div class="grid lg:grid-cols-2">
            <!-- Image side -->
            <div class="relative h-[400px] lg:h-auto overflow-hidden group">
              <NuxtImg src="/images/trail1.jpg" alt="Trail à Fontainebleau" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-linear-to-t from-black/60 via-transparent to-transparent flex items-end p-8">
                <div class="text-white">
                  <p class="text-xs uppercase tracking-widest font-bold mb-2 opacity-80">Seine-et-Marne</p>
                  <h3 class="text-3xl font-light italic">Elephant, Dame Jouane & 3 Pignons</h3>
                </div>
              </div>
            </div>

            <!-- Content side -->
            <div class="p-8 md:p-12 space-y-8 flex flex-col justify-between bg-white/40">
              <div class="space-y-6">
                <p class="text-lg text-gray-700 leading-relaxed font-light italic">
                  Partez à la découverte de cette forêt unique, du circuit des 25 bosses aux secteurs gardés plus secrets, pour allier technique et dépaysement.
                </p>
                
                <div class="grid gap-4">
                  <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/60 border border-white/80 shadow-sm">
                    <UIcon name="i-lucide-mountain" class="w-6 h-6 text-blue-600 shrink-0 mt-1" />
                    <div>
                      <h4 class="font-medium text-gray-950 italic">Formules Trail</h4>
                      <p class="text-sm text-gray-600">Initial trail, perfectionnement technique (montée/descente), trail roulant ou dynamique sur sentiers techniques.</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-4 p-4 rounded-2xl bg-white/60 border border-white/80 shadow-sm">
                    <UIcon name="i-lucide-compass" class="w-6 h-6 text-blue-600 shrink-0 mt-1" />
                    <div>
                      <h4 class="font-medium text-gray-950 italic">Randonnée Initiatique</h4>
                      <p class="text-sm text-gray-600">Une journée d'immersion pour découvrir les richesses géologiques et la biodiversité de la forêt.</p>
                    </div>
                  </div>
                </div>

                <div class="pt-8 border-t border-blue-100 grid sm:grid-cols-2 gap-8">
                  <div class="space-y-3">
                    <span class="text-xs uppercase tracking-widest text-blue-600 font-bold block mb-2">Inclus</span>
                    <ul class="text-sm text-gray-600 space-y-2">
                      <li class="flex gap-2">
                        <UIcon name="i-lucide-utensils" class="text-blue-500 mt-1" />
                        Repas inclus
                      </li>
                      <li class="flex gap-2">
                        <UIcon name="i-lucide-train" class="text-blue-500 mt-1" />
                        Navette Gare de Nemours
                      </li>
                    </ul>
                  </div>
                  <div class="space-y-1">
                    <span class="text-xs uppercase tracking-widest text-blue-600 font-bold block mb-2">Tarif à la journée</span>
                    <p class="text-3xl font-light text-gray-950">70 €</p>
                  </div>
                </div>
              </div>

              <div class="pt-6">
                <UButton to="mailto:antonine.rochet@hotmail.fr" size="xl" color="primary" block class="rounded-2xl py-4 shadow-xl shadow-blue-500/20 font-bold uppercase tracking-widest text-xs">
                  Réserver ma sortie
                </UButton>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Stage de Trail -->
      <section class="mt-32 border-t border-blue-100 pt-24">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-light text-gray-900 mb-6 italic">Stage d'initiation au Trail</h2>
          <p class="text-xl text-gray-600">3 jours face au Mont-Blanc — Secteur Sallanches</p>
          <div class="w-16 h-1 bg-blue-500/40 mx-auto rounded-full mt-8"></div>
        </div>

        <div class="bg-white/40 backdrop-blur-md rounded-3xl overflow-hidden border border-white/60 shadow-2xl max-w-6xl mx-auto">
          <div class="grid lg:grid-cols-2">
            <div class="relative h-[400px] lg:h-auto">
              <NuxtImg src="/images/mountain11.jpg" alt="Massif du Mont-Blanc" class="absolute inset-0 w-full h-full object-cover" />
              <div class="absolute inset-0 bg-linear-to-t from-black/60 to-transparent flex items-end p-8">
                <div class="text-white">
                  <p class="text-xs uppercase tracking-widest font-bold mb-2 opacity-80">Alpes françaises</p>
                  <h3 class="text-3xl font-light">Sallanches • Massif du Mont-Blanc</h3>
                </div>
              </div>
            </div>

            <div class="p-8 md:p-12 space-y-8">
              <div class="flex flex-wrap gap-3">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-100">
                  <UIcon name="i-lucide-calendar" /> Vendredi au Dimanche
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-100">
                  <UIcon name="i-lucide-mountain-snow" /> Initiation au Trail
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-600 text-white text-xs font-bold shadow-lg shadow-orange-600/20">
                  <UIcon name="i-lucide-users" /> Gaël & Antonine • AMM
                </span>
              </div>

              <div class="space-y-6">
                <div>
                  <h4 class="text-lg font-bold text-gray-950 mb-6 flex items-center gap-2 uppercase tracking-widest italic decoration-blue-500 decoration-2 underline-offset-8">
                    <span class="w-2 h-2 bg-blue-500 rounded-full"></span> Au programme
                  </h4>
                  <ul class="space-y-6 text-gray-700">
                    <li class="flex gap-4">
                      <div class="flex-none w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xs italic">
                        J1
                      </div>
                      <p><strong class="text-gray-950 block">Remise à l'effort</strong> Randonnée face au Mont-Blanc pour s'acclimater et éveiller le corps aux sentiers alpins.</p>
                    </li>
                    <li class="flex gap-4">
                      <div class="flex-none w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xs italic">
                        J2
                      </div>
                      <p><strong class="text-gray-950 block">Entraînement Trail</strong> Matinée technique sur les sentiers et ateliers pratiques l'après-midi.</p>
                    </li>
                    <li class="flex gap-4">
                      <div class="flex-none w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xs italic">
                        J3
                      </div>
                      <p><strong class="text-gray-950 block">Le Trail long</strong> Une sortie longue le matin pour mettre en pratique les techniques acquises dans un décor grandiose.</p>
                    </li>
                  </ul>
                </div>

                <div class="pt-8 border-t border-blue-100 grid sm:grid-cols-2 gap-8">
                  <div class="space-y-3">
                    <span class="text-xs uppercase tracking-widest text-blue-600 font-bold block mb-2">Compris / Non compris</span>
                    <ul class="text-sm text-gray-600 space-y-2">
                      <li class="flex gap-2">
                        <UIcon name="i-lucide-check" class="text-green-600 mt-1" />
                        Hébergement inclus
                      </li>
                      <li class="flex gap-2">
                        <UIcon name="i-lucide-x" class="text-red-500 mt-1" />
                        Autonomie repas & transports
                      </li>
                    </ul>
                  </div>
                  <div class="space-y-1">
                    <span class="text-xs uppercase tracking-widest text-blue-600 font-bold block mb-2">Tarifs</span>
                    <p class="text-3xl font-light text-gray-950">400 – 500 €</p>
                  </div>
                </div>
              </div>

              <div class="pt-4">
                <UButton to="mailto:antonine.rochet@hotmail.fr" size="xl" color="primary" block class="rounded-2xl py-4 shadow-xl shadow-blue-500/20">
                  Me contacter pour le dossier complet
                </UButton>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- Stage Yoga-Randonnée -->
      <section class="mt-32 border-t border-blue-100 pt-24 mb-16">
        <div class="text-center mb-16 px-4">
          <h2 class="text-4xl md:text-5xl font-light text-gray-900 mb-6 italic">Stage Yoga & Randonnée</h2>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto font-light">5 jours d'immersion entre effort en nature et introspection</p>
          <div class="w-24 h-1 bg-orange-500/40 mx-auto rounded-full mt-8"></div>
        </div>

        <div class="bg-white/40 backdrop-blur-md rounded-3xl overflow-hidden border border-white/60 shadow-2xl max-w-6xl mx-auto">
          <div class="flex flex-col lg:flex-row">
            <!-- Content side -->
            <div class="flex-1 p-8 md:p-12 flex flex-col justify-between">
              <div class="space-y-8">
                <div class="flex flex-wrap gap-3">
                  <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-50 text-orange-700 text-xs font-semibold border border-orange-100">
                    <UIcon name="i-lucide-calendar" /> 5 Jours
                  </span>
                  <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-50 text-orange-700 text-xs font-semibold border border-orange-100">
                    <UIcon name="i-lucide-leaf" /> Ressourcement & Calme
                  </span>
                  <span class="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-orange-600 text-white text-sm font-bold shadow-lg shadow-orange-600/20 leading-none">
                    <UIcon name="i-lucide-users" /> Marie-Émilie & Antonine
                  </span>
                </div>

                <div class="space-y-6">
                  <p class="text-xl text-gray-700 leading-relaxed font-light italic">
                    "Allier la précision du yoga Iyengar® à la mise en mouvement de la marche en nature pour apprécier l'effort, respirer l'air frais et se laisser imprégner des paysages."
                  </p>
                  
                  <div class="grid sm:grid-cols-2 gap-8 pt-4">
                    <div class="space-y-4">
                      <h4 class="text-sm font-bold text-gray-950 uppercase tracking-widest flex items-center gap-2">
                        <UIcon name="i-lucide-mountain" /> Pratique
                      </h4>
                      <ul class="space-y-2 text-gray-600 text-sm">
                        <li>• Pratique matinale de yoga actif</li>
                        <li>• Marche en nature, sentiers découverte</li>
                        <li>• Pratique de yoga restaurative en fin de journée</li>                        
                      </ul>
                    </div>
                    <div class="space-y-4">
                      <h4 class="text-sm font-bold text-gray-950 uppercase tracking-widest flex items-center gap-2">
                        <UIcon name="i-lucide-home" /> Inclus
                      </h4>
                      <ul class="space-y-2 text-gray-600 text-sm">
                        <li>• Hébergement complet</li>
                        <li>• Repas sains et équilibrés</li>
                        <li>• Lieu propice à la mise au calme</li>
                        <li>• Sorties trail possibles sur demande</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div class="pt-12 border-t border-orange-100/50 mt-12 flex flex-col sm:flex-row items-center justify-between gap-6">
                <div class="text-center sm:text-left">
                  <!-- <span class="text-xs uppercase tracking-widest text-orange-600 font-bold block mb-1">Inscriptions ouvertes</span> -->
                  <p class="text-sm text-gray-500 italic">Dossier complet sur demande</p>
                </div>
                <UButton to="mailto:antonine.rochet@hotmail.fr" size="xl" color="primary" class="rounded-2xl px-10 py-4 shadow-xl shadow-orange-500/20 font-bold">
                  Nous contacter
                </UButton>
              </div>
            </div>

            <!-- Image side -->
            <div class="lg:w-2/5 relative h-[300px] lg:h-auto order-first lg:order-last">
              <NuxtImg src="/images/yoga_outside_nature.png" alt="Retraite Yoga et Nature" class="absolute inset-0 w-full h-full object-cover" />
              <div class="absolute inset-0 bg-linear-to-l from-orange-950/20 to-transparent"></div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Sorties et Randonnées Guidées en Montagne | Antonine Rochet',
  description: 'Randonnées et sorties en montagne avec accompagnatrice diplômée : Fontainebleau, Jura, Vosges, Massif Central, Belledonne. Trail, rando, trek en Seine-et-Marne et massifs français.',
  keywords: 'randonnée guidée Fontainebleau, trail Seine-et-Marne, rando Jura, randonnée Vosges, accompagnatrice montagne, sortie montagne 77, trek France, randonnée guidée massif central, trail Fontainebleau, rando forêt'
})
</script>

