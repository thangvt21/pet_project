private void findOrderFileGenerated(
            Map<String, DistributeFileMoveDto> listFileMove) {
        Path folderPath = Paths.get(folder_name);
        log.info("findOrderFileGenerated : " + folder_name);
        try {
            if (!Files.exists(folderPath)) {
                log.info("findOrderFileGenerated not find folder " + folder_name);
            } else {
                Files.walk(folderPath)
                        .filter(Files::isRegularFile)
                        .filter(path -> path.getFileName().toString().contains(".pdf")
                                && !path.getFileName().toString().contains("_barcode.pdf"))
                        .forEach(path -> {
                            String fileName = path.getFileName().toString();
                            for (Map.Entry<String, DistributeFileMoveDto> entry : listFileMove.entrySet()) {
                                DistributeFileMoveDto item = entry.getValue();
                                String key = entry.getKey();
                                if (fileName.contains("_" + key + "_")) {
                                    log.info("findOrderFileGenerated file map: (" + key + " | " + fileName + ")");
                                    Map<String, Path> files = item.getFiles();
                                    files.put(fileName, path);
                                    item.setFiles(files);
                                    item.setTotalFinded(files.size());
                                }
                                listFileMove.put(key, item);
                            }
                        });
            }

        } catch (IOException e) {
            e.printStackTrace();
            log.error("findOrderFileGenerated ERROR  " + e.getMessage());
        }
    }

    private boolean moveFilesToDirectory(Map<String, Path> files, String destDirStr) {
        log.info("moveFilesToDirectory" + moving_folder_name);
        try {

            String path = moving_folder_name + "/" + destDirStr;
            Path destDir = Paths.get(path);

            log.info("moveFilesToDirectory: " + path);

            if (!Files.exists(destDir)) {
                log.info("moveFilesToDirectory create folder " + path);
                Files.createDirectories(destDir);
            }

            for (Map.Entry<String, Path> entry : files.entrySet()) {
                log.info("move file: " + entry.getKey());
                Path file = entry.getValue();
                Path targetPath = destDir.resolve(entry.getKey());
                Files.move(file, targetPath, StandardCopyOption.REPLACE_EXISTING);

                if (Files.size(targetPath) == 0) {
                    log.error("The file is 0 bytes after moving: " + entry.getKey());
                    if (!Files.exists(file)) {
                        log.error("The original file is no longer available: " + entry.getKey());
                    } else {log.info("Try to move a second time.");
                        Files.move(file, targetPath, StandardCopyOption.REPLACE_EXISTING);
                        log.info("Try to move a second time DONE.");
                    }
                    log.info("The file is 0 bytes after moving END.");
                }
            }

            return true;
        } catch (IOException e) {
            e.printStackTrace();
            log.error("Error moving file: " + e.getMessage());
        }
        return false;
    }