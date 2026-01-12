┌─────────────────────────────────────────────────────────┐
│                    Aplicación de Usuario                │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────┐
│                      langchain                          │
│  (Chains, Agents, Memory, Callbacks de alto nivel)      │
└─────────────────────────┬───────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
┌───────┴──────┐ ┌────────┴──────┐ ┌───────┴────────┐
│              │ │               │ │                │
│langchain-core│ │  langchain-   │ │Partner Packages│
│              │ │  community    │ │                │
│ Abstracciones│ │ Integraciones │ │ - openai       │
│ Interfaces   │ │ de terceros   │ │ - anthropic    │
│ LCEL         │ │               │ │ - ollama       │
│              │ │               │ │ - groq         │
└──────────────┘ └───────────────┘ └────────────────┘



langchain-core: Contiene las abstracciones fundamentales e interfaces base. Aquí están las clases abstractas como BaseLanguageModel, BasePromptTemplate, Runnable, y el corazón del LCEL (LangChain Expression Language). Es la base sobre la que se construye todo lo demás.

langchain-community: Integraciones con servicios y herramientas de terceros que no tienen soporte oficial optimizado. Incluye conectores para bases de datos vectoriales de código abierto, loaders de documentos, herramientas diversas, etc.

Partner Packages: Paquetes separados mantenidos oficialmente para integraciones específicas con proveedores principales (langchain-openai, langchain-anthropic, langchain-ollama, etc.).



STREAMLIT