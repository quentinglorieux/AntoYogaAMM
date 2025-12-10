import { defineContentConfig, defineCollection, z } from '@nuxt/content'

export default defineContentConfig({
    collections: {
        blog: defineCollection({
            type: 'page',
            source: 'blog/*.md',
            schema: z.object({
                title: z.string(),
                description: z.string(),
                image: z.string(),
                date: z.date(),
                head: z.object({
                    meta: z.array(z.object({
                        name: z.string(),
                        content: z.string()
                    })).optional()
                }).optional()
            })
        })
    }
})
