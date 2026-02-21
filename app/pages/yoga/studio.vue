<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">
    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-chaise-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-full w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(5%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(3deg);"
      />
    </div>

    <div class="relative z-10 max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-stone-950 italic mb-10">Le Studio</h1>

      <!-- Composition d'images du Studio (Editorial Offset) -->
      <div class="mb-32 md:mb-40 relative h-[500px] md:h-[750px] w-full max-w-5xl mx-auto mt-8 md:mt-12">
        
        <!-- Image Arrière Plan Gauche (Intérieur Studio Vide - Très gros) -->
        <div class="absolute left-0 top-0 md:top-[5%] w-[85%] md:w-[75%] h-[400px] md:h-[650px] shadow-[0_20px_50px_rgba(0,0,0,0.15)] z-10 group overflow-hidden bg-gray-100">
          <NuxtImg 
            src="/images/studio_vide.jpg" 
            alt="L'intérieur du studio" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-1000" 
            style="filter: sepia(0.2) saturate(1.15) contrast(1.1) brightness(1.05);"
          />
        </div>

        <!-- Image Premier Plan Droite (Anto - De tout son long) -->
        <div class="absolute right-0 top-0 w-[45%] md:w-[40%] h-full shadow-[0_30px_60px_rgba(0,0,0,0.3)] z-30 group overflow-hidden bg-gray-100">
          <NuxtImg 
            src="/images/studio_anto.png" 
            alt="Pratique de Yoga Iyengar dans le studio" 
            class="w-full h-full object-cover object-top transform group-hover:scale-[1.03] transition-transform duration-1000"
            style="filter: sepia(0.2) saturate(1.15) contrast(1.1) brightness(1.05);"
          />
        </div>

        <!-- Image Centrale Offset (Extérieur - Plus grande, au 1er plan) -->
        <div class="absolute left-[15%] md:left-[25%] bottom-[-20px] md:bottom-[10px] w-[65%] md:w-[45%] h-[250px] md:h-[420px] shadow-[0_30px_60px_rgba(0,0,0,0.25)] z-40 group overflow-hidden bg-gray-100">
          <NuxtImg 
            src="/images/studio-outside2.jpg" 
            alt="L'extérieur du studio à Larchant" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-1000" 
            style="filter: sepia(0.2) saturate(1.15) contrast(1.1) brightness(1.05);"
          />
        </div>
      </div>

      <div class="space-y-10 text-stone-800 leading-relaxed">
        <div class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <p class="text-lg italic text-stone-900">
            Le studio de yoga est un espace dédié à la pratique du yoga Iyengar, situé au cœur de Larchant dans un cadre paisible et lumineux. 
          </p>
        </div>

        <section class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <h2 class="text-3xl font-light text-stone-950 mb-4 mt-0 italic">Un espace de pratique</h2>
          <p>
            Le studio est entièrement équipé pour vous accueillir dans les meilleures conditions :
            briques, sangles, couvertures, chaises et **cordes murales** (*Yoga Kurunta*). 
            Tout le matériel nécessaire à la méthode Iyengar est à votre disposition.
          </p>
        </section>

        <section>
        <div class="text-center mx-auto mb-8 w-full md:w-auto">
          <h2 class="text-3xl font-light text-stone-950 italic m-0">Horaires des cours au studio</h2>
        </div>
        
        <div class="grid md:grid-cols-2 gap-6">
            <!-- Lundi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Lundi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">10h45 – 12h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">12h30 – 14h00</p>
                    <p class="text-orange-900/80 italic text-sm">Intermédiaire / Avancé</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mardi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Mardi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">18h30 – 20h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">20h00 – 21h00</p>
                    <p class="text-orange-900/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mercredi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Mercredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-stone-900">18h30 – 20h00</p>
                  <p class="text-orange-900/80 italic text-sm">Intermédiaire / Avancé</p>
                </div>
              </div>
            </div>

            <!-- Jeudi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Jeudi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">12h30 – 13h30</p>
                    <p class="text-orange-900/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">18h30 – 20h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Vendredi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Vendredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-corde-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-stone-900">12h00 – 13h00</p>
                  <p class="text-orange-900/80 italic text-sm">Yoga adapté</p>
                </div>
              </div>
            </div>

            <!-- Lien Cours Extérieurs -->
            <div class="bg-white rounded-2xl shadow-sm p-6 border border-orange-500/30 flex flex-col justify-center items-center text-center">
              <p class="text-stone-950 font-light italic mb-4">Antonine intervient aussi à Nemours et Le Vaudoué.</p>
              <UButton to="/yoga/cours" color="primary" variant="solid" size="lg" icon="i-heroicons-calendar">
                Voir tous les cours
              </UButton>
            </div>
          </div>
        </section>

        <section class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <h2 class="text-3xl font-light text-stone-950 mb-4 mt-0 italic">Accès</h2>
          <div class="flex flex-col sm:flex-row gap-8 items-center">
            <div class="flex-1">
              <p class="text-lg mb-2">
                <strong>16 Place des Tilleuls, 77760 Larchant.</strong>
              </p>
              <p class="text-orange-900 mb-4 italic">
                Au cœur du village, face à l'église. Entrez sans frapper ! 
              </p>
              <p class="text-stone-600 text-sm">
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
