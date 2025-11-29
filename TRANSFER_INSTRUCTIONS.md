# Transfer MS MARCO Data Files from Local to SSH Server

## Quick Transfer Command

Run this command **from your LOCAL machine** (not on the SSH server):

```bash
rsync -avz --progress /home/necromancer/Downloads/gopalakt/required/ kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/
```

Or if you prefer `scp`:

```bash
scp -r /home/necromancer/Downloads/gopalakt/required/* kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/
```

## What Should Be Transferred

Make sure these files/folders are in the `required` directory:
- `full_collection/` (directory)
- `dev_qrel.json`
- `TREC_DL_2019/` (directory)
- `TREC_DL_2020/` (directory)
- `dev_queries/` (directory)

## After Transfer

Once the files are transferred, I can verify they're in the correct location and help you run the inference.

## Alternative: If Files Are in Archive

If your files are in a zip/tar archive:

1. Transfer the archive:
   ```bash
   scp /home/necromancer/Downloads/gopalakt/required.zip kmirakho@gretel:/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/
   ```

2. Then on the server, extract it:
   ```bash
   cd /data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/
   unzip required.zip  # or tar -xzf required.tar.gz
   ```

## Server Details

- **Server**: gretel
- **User**: kmirakho
- **Target Path**: `/data/kmirakho/Gopal/PAG/PAG/data/msmarco-full/`

