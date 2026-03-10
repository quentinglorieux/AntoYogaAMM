<template>
  <div class="relative h-screen overflow-hidden">
    <HeroSliderImg />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'home'
})

useSeoMeta({
  title: 'Antonine Rochet - Yoga Iyengar & Accompagnatrice en Montagne | Larchant, Le Vaudoué, Nemours',
  description: 'Cours de yoga Iyengar® à Larchant, Nemours et Le Vaudoué. Randonnées et sorties montagne avec accompagnatrice diplômée en Seine-et-Marne et massifs français.',
  ogTitle: 'Antonine Rochet - Yoga Iyengar & Accompagnatrice en Montagne',
  ogDescription: 'Professeure de yoga Iyengar® et accompagnatrice en montagne diplômée. Cours de yoga et randonnées guidées.',
  ogImage: '/images/anto4.jpg',
  ogType: 'website',
  twitterCard: 'summary_large_image',
  keywords: 'yoga Larchant, yoga Iyengar® Seine-et-Marne, cours yoga Nemours, yoga Le Vaudoué, accompagnatrice montagne, randonnée Fontainebleau, trail Seine-et-Marne, sorties montagne, yoga 77, stage yoga, yoga débutant'
})
</script>
