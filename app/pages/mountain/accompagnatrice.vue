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

    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="text-center mb-16">
        <h1 class="text-5xl font-light text-gray-900 mb-4">L'Accompagnatrice en Montagne</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Antonine Rochet, accompagnatrice diplômée
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-12 items-start">
        <div class="rounded-xl overflow-hidden shadow-2xl">
          <NuxtImg 
            src="/images/trail2.jpg" 
            alt="Antonine Rochet - Accompagnatrice en montagne" 
            class="w-full h-[500px] object-cover"
          />
        </div>

        <div class="space-y-6">
          <div class="prose prose-lg max-w-none">
            <h2 class="text-3xl font-light text-gray-900 mb-4">Passionnée de montagne</h2>
            <p class="text-gray-700 leading-relaxed">
              Diplômée accompagnatrice en montagne, je partage ma passion pour la nature et les grands espaces.
            </p>
            <p class="text-gray-700 leading-relaxed">
              Mon expérience me permet de vous guider en toute sécurité dans les massifs du Jura, des Vosges, du Massif Central et de Belledonne.
            </p>
          </div>
          
          <div class="mt-8">
            <UButton to="/mountain/sorties" size="lg" color="primary" variant="solid">
              Voir les sorties
            </UButton>
          </div>
        </div>
      </div>

      <!-- Section Aller plus vite -->
      <section class="mt-24 border-t border-blue-100 pt-20">
        <div class="text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-light text-gray-900 mb-6 italic">Aller plus vite</h2>
          <div class="w-16 h-1 bg-blue-500/40 mx-auto rounded-full"></div>
        </div>
        
        <div class="max-w-3xl mx-auto mb-16 px-4">
          <p class="text-xl md:text-2xl text-gray-700 leading-relaxed text-center font-light">
            "Le trail est  comme une extension naturelle de la marche en montagne. Laisser son gros sac pour s'alléger, sentir l'air qui file sur le visage et les bras, 
            lâcher prise dans les descentes, rythmer les montées avec le souffle, voir les abords du sentier qui défilent et les reliefs lointains qui nous stabilisent. C’est l’art d’allier vitesse et paysages grandioses, où la respiration devient le métronome de l’effort. Rejoignez-moi pour que courir vous devienne accessible et de plus en plus aisé"
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto px-4">
          <!-- Course 1 -->
          <div class="relative group overflow-hidden bg-white/40 backdrop-blur-md rounded-3xl p-8 border border-white/60 shadow-xl transition-all duration-500 hover:bg-white/70 hover:-translate-y-1">
             <div class="absolute -top-4 -right-4 p-8 opacity-5 group-hover:opacity-10 transition-opacity">
               <UIcon name="i-lucide-trophy" class="text-8xl" />
             </div>
             
             <h3 class="text-2xl font-medium text-gray-950 mb-8 border-b border-blue-500/20 pb-4">Les 16 km Verts du Vaudoué</h3>
             
             <div class="space-y-6">
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Distance & D+</span>
                 <span class="text-lg text-gray-900 font-medium">16 km • 160m D+</span>
               </div>
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Classement</span>
                 <span class="text-lg text-gray-900 font-medium">23ème féminine</span>
               </div>
               <div class="flex justify-between items-end">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Chrono</span>
                 <div class="text-right">
                  <span class="text-3xl font-light text-gray-950">1h27</span>
                  <div class="text-xs text-gray-500 font-medium italic mt-1">5,27 min/km</div>
                 </div>
               </div>
             </div>
          </div>

          <!-- Course 2 -->
          <div class="relative group overflow-hidden bg-white/40 backdrop-blur-md rounded-3xl p-8 border border-white/60 shadow-xl transition-all duration-500 hover:bg-white/70 hover:-translate-y-1">
             <div class="absolute -top-4 -right-4 p-8 opacity-5 group-hover:opacity-10 transition-opacity">
               <UIcon name="i-lucide-trophy" class="text-8xl" />
             </div>
             
             <h3 class="text-2xl font-medium text-gray-950 mb-8 border-b border-blue-500/20 pb-4">Hivernal du Sancy / Mont-Dore</h3>
             
             <div class="space-y-6">
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Distance & D+</span>
                 <span class="text-lg text-gray-900 font-medium">33 km • 1600m D+</span>
               </div>
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Classement</span>
                 <span class="text-lg text-gray-900 font-medium">19ème féminine</span>
               </div>
               <div class="flex justify-between items-end">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Chrono</span>
                 <div class="text-right">
                  <span class="text-3xl font-light text-gray-950">5h47</span>
                  <div class="text-xs text-gray-500 font-medium italic mt-1">10,5 min/km</div>
                 </div>
               </div>
             </div>
          </div>

          <!-- Course 3 -->
          <div class="relative group overflow-hidden bg-white/40 backdrop-blur-md rounded-3xl p-8 border border-white/60 shadow-xl transition-all duration-500 hover:bg-white/70 hover:-translate-y-1">
             <div class="absolute -top-4 -right-4 p-8 opacity-5 group-hover:opacity-10 transition-opacity">
               <UIcon name="i-lucide-trophy" class="text-8xl" />
             </div>
             
             <h3 class="text-2xl font-medium text-gray-950 mb-8 border-b border-blue-500/20 pb-4">Lyricantrail</h3>
             
             <div class="space-y-6">
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Distance & D+</span>
                 <span class="text-lg text-gray-900 font-medium">14 km • 500m D+</span>
               </div>
               <div class="flex justify-between items-end border-b border-gray-100/50 pb-2">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Classement</span>
                 <span class="text-lg text-gray-900 font-medium">10ème féminine</span>
               </div>
               <div class="flex justify-between items-end">
                 <span class="text-xs uppercase tracking-widest text-blue-600 font-bold">Chrono</span>
                 <div class="text-right">
                  <span class="text-3xl font-light text-gray-950">1h37</span>
                  <div class="text-xs text-gray-500 font-medium italic mt-1">6,9 min/km</div>
                 </div>
               </div>
             </div>
          </div>
        </div>
      </section>

      <!-- Section Se repérer -->
      <section class="mt-24 border-t border-blue-100 pt-20 pb-24">
        <div class="text-center mb-12 px-4">
          <h2 class="text-4xl md:text-5xl font-light text-gray-900 mb-6 italic">Se repérer</h2>
          <div class="w-16 h-1 bg-blue-500/40 mx-auto rounded-full"></div>
        </div>
        
        <div class="max-w-3xl mx-auto mb-16 px-4">
          <p class="text-xl md:text-2xl text-gray-700 leading-relaxed text-center font-light">
            "Une boussole, une carte et notre environnement : comment passer de l'un à l'autre pour guider nos pas ? L'orientation est un dialogue constant avec le terrain, une lecture fine des reliefs et des courbes pour tracer son propre chemin en toute autonomie. La forêt de Fontainebleau est un magnifique et complexe terrain d'entrainement pour préparer aux courses d'orientation (O'Bivwak 2019, 2022, 2024 et 2026)"
          </p>
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
  title: 'Antonine Rochet - Accompagnatrice en Montagne Diplômée | Guide Rando',
  description: 'Antonine Rochet, accompagnatrice en montagne diplômée et professeure de yoga Iyengar. Randonnées guidées en Seine-et-Marne, Jura, Vosges et Massif Central. Trail et trek en forêt de Fontainebleau.',
  keywords: 'accompagnatrice montagne diplômée, guide montagne Fontainebleau, accompagnatrice rando 77, guide randonnée Seine-et-Marne, AMM diplômée, guide nature, accompagnateur montagne'
})
</script>
