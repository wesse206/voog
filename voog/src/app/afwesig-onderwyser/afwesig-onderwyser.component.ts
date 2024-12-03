import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './afwesig-onderwyser.component.html',
  styleUrl: './afwesig-onderwyser.component.css'
})
export class AfwesigOnderwyserComponent implements OnInit {
  lookupForm = new FormGroup({
    teacherCode: new FormControl(''),
    day: new FormControl(''),
  });

  absentTeachers = null
  teacherlessLearners = null

  onSubmit() {
    let TeacherCode = String(this.lookupForm.value['teacherCode'])
    let Day = Number(this.lookupForm.value['day'])
    
    this.api.getTeacherlessLearners(TeacherCode, Day).subscribe(data => {
      this.teacherlessLearners = data
      this.api.setAbsentTeacher(TeacherCode, Day).subscribe(data => {
        this.absentTeachers = data
      })
    })
  }

  removeAbsence(TeacherCode: string, Day: number) {
    this.api.removeAbsentTeacher(TeacherCode, Day).subscribe(data => {
      this.absentTeachers = data
    })
    
  }

  ngOnInit(): void {
    this.api.getAbsentTeachers().subscribe(data => {
      this.absentTeachers = data
    })
  }

  constructor(private http: HttpClient, private api: ApiService) { }

}

