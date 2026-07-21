import { useState, useCallback } from 'react'
import { useDropzone } from 'react-dropzone'
import { Upload, X, File, Image as ImageIcon } from 'lucide-react'
import { toast } from 'sonner'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import apiClient from '@/lib/axios'

export function UploadPage() {
  const [files, setFiles] = useState<File[]>([])
  const [uploading, setUploading] = useState(false)

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setFiles((prev) => [...prev, ...acceptedFiles])
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.png', '.jpg', '.jpeg', '.gif', '.webp'],
      'application/pdf': ['.pdf'],
      'text/csv': ['.csv'],
      'application/json': ['.json'],
    },
    maxSize: 5 * 1024 * 1024, // 5MB
  })

  const removeFile = (index: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== index))
  }

  const uploadFiles = async () => {
    if (files.length === 0) return

    setUploading(true)
    const formData = new FormData()

    if (files.length === 1) {
      formData.append('file', files[0])
      try {
        await apiClient.post('/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        toast.success('File uploaded successfully!')
        setFiles([])
      } catch (error: any) {
        toast.error(error.response?.data?.detail || 'Upload failed')
      }
    } else {
      files.forEach((file) => formData.append('files', file))
      try {
        await apiClient.post('/upload/multiple', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        toast.success(`${files.length} files uploaded successfully!`)
        setFiles([])
      } catch (error: any) {
        toast.error(error.response?.data?.detail || 'Upload failed')
      }
    }
    setUploading(false)
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">File Upload</h1>
        <p className="text-muted-foreground mt-1">
          Drag and drop files or click to browse
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Upload Files</CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Drop Zone */}
          <div
            {...getRootProps()}
            className={`border-2 border-dashed rounded-lg p-12 text-center cursor-pointer transition-colors ${
              isDragActive
                ? 'border-primary bg-primary/5'
                : 'border-muted-foreground/25 hover:border-primary/50'
            }`}
          >
            <input {...getInputProps()} />
            <Upload className="mx-auto h-12 w-12 text-muted-foreground/50" />
            <p className="mt-4 text-sm text-muted-foreground">
              {isDragActive
                ? 'Drop files here...'
                : 'Drag & drop files here, or click to select'}
            </p>
            <p className="mt-2 text-xs text-muted-foreground">
              Max file size: 5MB. Supported: Images, PDF, CSV, JSON
            </p>
          </div>

          {/* File List */}
          {files.length > 0 && (
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-medium">
                  {files.length} file{files.length > 1 ? 's' : ''} selected
                </h3>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => setFiles([])}
                  className="text-muted-foreground"
                >
                  Clear all
                </Button>
              </div>
              <div className="space-y-2">
                {files.map((file, index) => (
                  <div
                    key={`${file.name}-${index}`}
                    className="flex items-center justify-between p-3 rounded-lg bg-muted/50"
                  >
                    <div className="flex items-center gap-3">
                      {file.type.startsWith('image/') ? (
                        <ImageIcon className="h-5 w-5 text-blue-500" />
                      ) : (
                        <File className="h-5 w-5 text-muted-foreground" />
                      )}
                      <div>
                        <p className="text-sm font-medium">{file.name}</p>
                        <p className="text-xs text-muted-foreground">
                          {(file.size / 1024).toFixed(1)} KB
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      {file.type.startsWith('image/') && (
                        <Badge variant="secondary" className="text-xs">
                          Image
                        </Badge>
                      )}
                      <Button
                        variant="ghost"
                        size="icon"
                        onClick={() => removeFile(index)}
                        className="h-8 w-8"
                      >
                        <X className="h-4 w-4" />
                      </Button>
                    </div>
                  </div>
                ))}
              </div>
              <Button
                onClick={uploadFiles}
                disabled={uploading}
                className="w-full"
              >
                {uploading
                  ? 'Uploading...'
                  : `Upload ${files.length > 1 ? `All ${files.length} Files` : 'File'}`}
              </Button>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
