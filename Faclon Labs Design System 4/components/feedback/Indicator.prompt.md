Status light: a coloured dot with a neutral-grey label. Use inside tables and dense lists where a Badge would shout.

```jsx
<Indicator intent="positive">Active</Indicator>
<Indicator intent="negative" showLabel={false} />
```

- `intent`: positive | negative | notice | information | neutral
- `size`: small | medium | large. Only Small (16px row, 6px dot, 12/18 label) is fully specified in the source Figma; medium/large scale the dot to 8/10px against the token heights (20px).
- The label always uses `--text-subtle`, never the intent colour — colour lives in the dot only.
