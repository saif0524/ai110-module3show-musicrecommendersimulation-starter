const flowchart = `flowchart TD
    A[Start] --> B[Get User Preferences]
    B --> C[Load songs.csv]
    C --> D[Read one song row]
    D --> E[Compute score for this song]
    E --> E1[Genre match +2.0]
    E --> E2[Mood match +1.0]
    E --> E3[Energy similarity points]
    E --> E4[Acoustic preference bonus]
    E1 --> F[Store song + score + reason]
    E2 --> F
    E3 --> F
    E4 --> F
    F --> G{More songs left?}
    G -- Yes --> D
    G -- No --> H[Sort all songs by score descending]
    H --> I[Take Top K]
    I --> J[Output ranked recommendations]
`;

export default flowchart;
