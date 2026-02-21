<template>
  <div class="relative min-h-screen bg-linear-to-br from-green-50 to-teal-100 overflow-hidden">
    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-chaise-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-full w-auto object-contain"
        style="opacity: 0.12; filter: grayscale(10%) sepia(5%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(3deg);"
      />
    </div>

    <div class="relative z-10 max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-teal-900 mb-10 italic">Le Studio</h1>

      <div class="flex justify-center mb-12">
        <div class="w-full md:w-1/2 rounded-2xl overflow-hidden shadow-2xl transform hover:scale-[1.02] transition-transform duration-500">
          <NuxtImg src="/images/studio3.jpeg" alt="Le Studio de yoga Iyengar" class="w-full h-auto object-cover" />
        </div>
      </div>

      <div class="space-y-10 text-gray-700 leading-relaxed">
        <div class="bg-white/40 backdrop-blur-md rounded-2xl p-8 border border-white/30">
          <p class="text-lg italic text-teal-950">
            Le studio de yoga est un espace dédié à la pratique du yoga Iyengar, situé au cœur de Larchant dans un cadre paisible et lumineux. 
          </p>
        </div>

        <section class="bg-white/30 backdrop-blur-sm rounded-2xl p-8 border border-white/20">
          <h2 class="text-3xl font-light text-teal-900 mb-4 mt-0 italic">Un espace de pratique</h2>
          <p>
            Le studio est entièrement équipé pour vous accueillir dans les meilleures conditions :
            briques, sangles, couvertures, chaises et **cordes murales** (*Yoga Kurunta*). 
            Tout le matériel nécessaire à la méthode Iyengar est à votre disposition.
          </p>
        </section>

        <section>
          <h2 class="text-3xl font-light text-teal-900 mb-6 italic text-center">Horaires des cours au studio</h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <!-- Lundi -->
            <div class="bg-white/40 backdrop-blur-lg rounded-2xl shadow-lg p-6 border border-white/40 border-l-4 border-l-teal-500/50">
              <h3 class="text-xl font-light text-teal-900 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-teal-500 rounded-full"></span> Lundi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">10h45 – 12h00</p>
                    <p class="text-teal-800/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">12h30 – 14h00</p>
                    <p class="text-teal-800/80 italic text-sm">Intermédiaire / Avancé</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mardi -->
            <div class="bg-white/40 backdrop-blur-lg rounded-2xl shadow-lg p-6 border border-white/40 border-l-4 border-l-teal-500/50">
              <h3 class="text-xl font-light text-teal-900 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-teal-500 rounded-full"></span> Mardi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">18h30 – 20h00</p>
                    <p class="text-teal-800/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">20h00 – 21h00</p>
                    <p class="text-teal-800/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mercredi -->
            <div class="bg-white/40 backdrop-blur-lg rounded-2xl shadow-lg p-6 border border-white/40 border-l-4 border-l-teal-500/50">
              <h3 class="text-xl font-light text-teal-900 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-teal-500 rounded-full"></span> Mercredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-teal-950">18h30 – 20h00</p>
                  <p class="text-teal-800/80 italic text-sm">Intermédiaire / Avancé</p>
                </div>
              </div>
            </div>

            <!-- Jeudi -->
            <div class="bg-white/40 backdrop-blur-lg rounded-2xl shadow-lg p-6 border border-white/40 border-l-4 border-l-teal-500/50">
              <h3 class="text-xl font-light text-teal-900 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-teal-500 rounded-full"></span> Jeudi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">12h30 – 13h30</p>
                    <p class="text-teal-800/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-teal-950">18h30 – 20h00</p>
                    <p class="text-teal-800/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Vendredi -->
            <div class="bg-white/40 backdrop-blur-lg rounded-2xl shadow-lg p-6 border border-white/40 border-l-4 border-l-teal-500/50">
              <h3 class="text-xl font-light text-teal-900 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-teal-500 rounded-full"></span> Vendredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-white/60 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-corde-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-teal-950">12h00 – 13h00</p>
                  <p class="text-teal-800/80 italic text-sm">Yoga adapté</p>
                </div>
              </div>
            </div>

            <!-- Lien Cours Extérieurs -->
            <div class="bg-teal-900/10 backdrop-blur-lg rounded-2xl p-6 border border-teal-500/20 flex flex-col justify-center items-center text-center">
              <p class="text-teal-900 font-light italic mb-4">Antonine intervient aussi à Nemours et Le Vaudoué.</p>
              <UButton to="/yoga/cours" color="primary" variant="solid" size="lg" icon="i-heroicons-calendar">
                Voir tous les cours
              </UButton>
            </div>
          </div>
        </section>

        <section class="bg-white/30 backdrop-blur-sm rounded-2xl p-8 border border-white/20">
          <h2 class="text-3xl font-light text-teal-900 mb-4 mt-0 italic">Accès</h2>
          <div class="flex flex-col sm:flex-row gap-8 items-center">
            <div class="flex-1">
              <p class="text-lg mb-2">
                **16 Place des Tilleuls, 77760 Larchant.**
              </p>
              <p class="text-teal-800 mb-4 italic">
                Au cœur du village, face à l'église. Entrez sans frapper ! 
              </p>
              <p class="text-gray-600 text-sm">
                Des vestiaires et des sanitaires sont à votre disposition pour vous changer sur place.
              </p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Le Studio de Yoga Iyengar à Larchant | Antonine Rochet',
  description: 'Studio de yoga Iyengar à Larchant près de Fontainebleau. Cours collectifs et particuliers tous niveaux. Planning des cours à La Chapelle-la-Reine, Nemours et Le Vaudoué. Seine-et-Marne 77.',
  keywords: 'studio yoga Larchant, yoga Iyengar Fontainebleau, cours yoga Seine-et-Marne, yoga 77, planning cours yoga, yoga Nemours, yoga La Chapelle-la-Reine, studio yoga 77'
})
</script>
