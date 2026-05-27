# fatigue-test-setup-repo

Repository layout created for the fatigue pressure chamber data collection setup.

## Layout

```text
fatigue-test-setup-repo/
├── README.md
├── paper/
│   └── figures/
├── cad/
│   ├── solidworks/control_board/
│   └── exports/
│       ├── step/
│       └── stl/
├── src/fatigue_test_setup/
│   ├── acquire_images.py
│   └── images_to_video.py
├── scripts/
│   ├── acquire_images.py
│   └── images_to_video.py
├── configs/
├── docs/
├── protocols/
├── data/
│   ├── raw/
│   ├── processed/
│   └── examples/
├── examples/
└── tests/
```

## Notes

- Directory scaffolding was created with real folders only.
- Image acquisition and image-to-video conversion scripts were added in both `src/` and `scripts/`.
