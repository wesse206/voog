import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VoogComponent } from './voog.component';

describe('VoogComponent', () => {
  let component: VoogComponent;
  let fixture: ComponentFixture<VoogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VoogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VoogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
