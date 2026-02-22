<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">

    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-corde2-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-[110%] w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(10%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(-12deg);"
      />
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 relative z-10">
      <h1 class="text-5xl font-light text-stone-950 mb-10">Les Cours</h1>

      <div class="space-y-8">
        <div class="grid lg:grid-cols-2 gap-8">
          <!-- Au studio de Larchant -->
          <section class="space-y-6">

              <h2 class="text-3xl font-light text-stone-950 mb-8">Au studio de Larchant</h2>

            <div class="space-y-6 relative">
              <!-- Trait continu vertical entre les cases, en avant-plan -->
              <div class="absolute left-0 top-0 bottom-0 w-1 bg-orange-400 z-20 rounded-full"></div>

              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 flex items-start gap-4 relative z-10">
                <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                  <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="Pratique intermédiaire / avancé"
                    class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div class="flex-1">
                  <h3 class="text-xl font-medium text-stone-950">Pratique intermédiaire / avancé</h3>
                  <ul class="mt-2 space-y-1 text-stone-900">
                    <li>Lundi — 12h30–14h00</li>
                    <li>Mercredi — 18h30–20h00</li>
                  </ul>
                </div>
              </div>

              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 flex items-start gap-4 relative z-10">
                <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                  <NuxtImg src="/images/lulu-brique-nobg.png" alt="Yoga doux" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div class="flex-1">
                  <h3 class="text-xl font-medium text-stone-950">Yoga doux</h3>
                  <ul class="mt-2 space-y-1 text-stone-900">
                    <li>Mardi — 20h00-21h00</li>
                    <li>Jeudi — 12h30–13h30</li>
                  </ul>
                </div>
              </div>

              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 flex items-start gap-4 relative z-10">
                <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                  <NuxtImg src="/images/lulu-om-nobg.png" alt="Pratique débutant / intermédiaire"
                    class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div class="flex-1">
                  <h3 class="text-xl font-medium text-stone-950">Pratique débutant / intermédiaire</h3>
                  <ul class="mt-2 space-y-1 text-stone-900">
                    <li>Lundi — 10h45-12h00</li>
                    <li>Mardi — 18h30-20h00</li>
                    <li>Jeudi — 18h30–20h00</li>
                  </ul>
                </div>
              </div>

              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 flex items-start gap-4 relative z-10">
                <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                  <NuxtImg src="/images/lulu-corde-nobg.png" alt="Yoga adapté" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div class="flex-1">
                  <h3 class="text-xl font-medium text-stone-950">Yoga adapté</h3>
                  <ul class="mt-2 space-y-1 text-stone-900">
                    <li>Vendredi — 12h00–13h00</li>
                  </ul>
                </div>
              </div>
            </div>
          </section>


          <!-- Dans d'autres lieux -->
          <section class="space-y-6">

              <h2 class="text-3xl font-light text-stone-950 mb-8">Dans d'autres lieux</h2>

            <div class="space-y-6 relative">
              <!-- Trait continu vertical entre les cases, en avant-plan -->
              <div class="absolute left-0 top-0 bottom-0 w-1 bg-orange-400 z-20 rounded-full"></div>

              <!-- Nemours -->
              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 relative z-10">
                <div class="flex items-start gap-4">
                  <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                    <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="Nemours" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div class="flex-1">
                    <h3 class="text-2xl font-light text-stone-950">Nemours</h3>
                    <span class="text-sm text-orange-600">Débutant / intermédiaire</span>
                    <ul class="mt-3 space-y-1 text-stone-900">
                      <li>Jeudi — 10h00–11h30</li>
                    </ul>
                    <div class="mt-4 text-stone-800">
                      <p class="font-medium">Magic Form</p>
                      <p>37 avenue Carnot<br />77140 Nemours</p>
                    </div>
                    <div class="mt-4">
                      <UButton to="https://magic-form.fr/clubs/saint-pierre-les-nemours" target="_blank" rel="noopener"
                        color="primary" variant="soft">
                        En savoir plus
                      </UButton>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Le Vaudoué -->
              <div class="bg-white/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 relative z-10">
                <div class="flex items-start gap-4">
                  <div class="w-16 h-16 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative mt-1">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="Le Vaudoué" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div class="flex-1">
                    <h3 class="text-2xl font-light text-stone-950">Le Vaudoué</h3>
                    <span class="text-sm text-orange-600">Débutant / intermédiaire</span>
                    <ul class="mt-3 space-y-1 text-stone-900">
                      <li>Lundi — 19h00–20h30</li>
                    </ul>
                    <div class="mt-4 text-stone-800">
                      <p class="font-medium">ESF77</p>
                    </div>
                    <div class="mt-4">
                      <UButton to="https://magic-form.fr/clubs/saint-pierre-les-nemours" target="_blank" rel="noopener"
                        color="primary" variant="soft">
                        En savoir plus
                      </UButton>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>


        <!-- À domicile -->
        <section class="bg-white shadow-sm rounded-2xl p-6 border border-stone-200/60 space-y-4 relative overflow-hidden">
          <h2 class="text-3xl font-light text-stone-950">À domicile</h2>
          <ul class="list-disc pl-5 text-stone-900 space-y-1">
            <li>Cours postural — seul·e ou à plusieurs</li>
            <li>Yoga pré et post-natal — pour accompagner votre grossesse et ses suites</li>
            <li>Pranayama — explorez votre respiration et relâchez votre esprit</li>
          </ul>
          <div class="pt-2">
            <UButton to="mailto:yoga@antoninerochet.fr" color="primary">Me contacter</UButton>
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
  title: 'Cours de Yoga Iyengar à Larchant, Fontainebleau, Nemours | Planning & Horaires',
  description: 'Tous les cours de yoga Iyengar avec Antonine Rochet : Larchant, La Chapelle-la-Reine, Nemours, Le Vaudoué. Planning détaillé, horaires et lieux. Cours tous niveaux débutant à avancé.',
  keywords: 'cours yoga Larchant, horaires yoga Fontainebleau, planning yoga Nemours, cours yoga 77, yoga débutant Seine-et-Marne, cours yoga Iyengar collectif, yoga La Chapelle-la-Reine horaires, cours yoga Le Vaudoué'
})
</script>
